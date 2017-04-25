import validators
from lxml import etree
from requests import ConnectionError
import re
import logging

logger = logging.getLogger(__name__)


def validate_url(url):
    """
    Validates the URL
    :param url:
    :return:
    """
    if validators.url(url):
        return url
    elif validators.domain(url):
        return "http://{}".format(url)
    return ""


def validate_repo_url(url):
    """
    Validates and formats `url` to be valid URL pointing to a repo on bitbucket.org or github.com
    :param url: str, URL
    :return: str, valid URL if valid repo, emptry string otherwise
    """
    try:
        if "github.com" in url:
            return re.findall(r"https?://w?w?w?.?github.com/[\w\-]+/[\w.-]+", url)[0]
        elif "bitbucket.org" in url:
            return re.findall(r"https?://bitbucket.org/[\w.-]+/[\w.-]+", url)[0] + "/src/"
        elif "launchpad.net" in url:
            return re.findall(r"https?://launchpad.net/[\w.-]+", url)[0]
        elif "sourceforge.net" in url:
            mo = re.match(r"https?://sourceforge.net/projects/"
                          r"([\w.-]+)/", url, re.I)
            template = "https://sourceforge.net/p/{}/code/HEAD/tree/trunk/src/"
            return template.format(mo.groups()[0])
    except (IndexError, AttributeError):
        pass
    return ""


def contains_project_name(name, link):
    """
    Checks if the given link `somewhat` contains the project name.
    :param name: str, project name
    :param link: str, link
    :return: bool, True if the link contains the project name
    """
    def unclutter(string):
        # strip out all python references and remove all excessive characters
        string = string.lower().replace("python-", "").replace("py-", "")
        return re.sub("[^0123456789 a-zA-Z]", "", string).strip()
    return unclutter(name) in unclutter(link)


def find_repo_urls(session, name, candidates):
    """
    Visits the given URL candidates and searches the page for valid links to a repository.
    :param session: requests Session instance
    :param name: str, project name
    :param candidates: list, list of URL candidates
    :return: str, URL to a repo
    """
    for _url in candidates:
        if validate_url(_url):
            try:
                resp = session.get(_url)
                if resp.status_code == 200:
                    tree = etree.HTML(resp.content)
                    for link in frozenset([str(l) for l in tree.xpath("//a/@href")]):
                        # check if the link 1) is to github.com / bitbucket.org AND 2) somewhat
                        # contains the project name
                        if ("github.com" in link or "bitbucket.org" in link or
                                "sourceforge.net" in link) \
                                and contains_project_name(name, link):
                            link = validate_url(validate_repo_url(url=link))
                            if link:
                                logger.debug("Found repo URL {}".format(link))
                                yield link
            except ConnectionError:
                # we really don't care about connection errors here. a lot of project pages are simply
                # down because the project is no longer maintained
                pass

# changelogs come in all forms and colors. This set contains most of them, e.g. (HISTORY, history,
# History.md, HISTORY.rst ... etc.)
CHANGELOG_FILENAME_CANDIDATES = frozenset([
    item for sublist in [
        [f + e, f.upper() + e, f.capitalize() + e] for f in [
            "history", "news", "releases", "release", "changes",
            "changelog", "log"
        ] for e in [
            "", ".txt", ".md", ".rst", ".adoc"
        ]
        ] for item in sublist
] + ["ReleaseNotes.wiki"])

DOCS_CANDIDATES = frozenset([
    "docs", "doc", "documentation", "docs-src", "wiki",
    "docs/", "doc/", "documentation/", "docs-src/", "wiki/"
])


def find_changelog(session, repo_url, deep=True):
    """
    Tries to find changelogs on the given `repo_url`.
    :param session: requests Session instance
    :param repo_url: str, URL to the repo
    :param deep: bool, deep search
    :return: str, URL to the raw changelog content
    """
    logger.debug("Trying to find changelog on repo {}".format(repo_url))
    resp = session.get(repo_url)
    if resp.status_code == 200:
        # build up a list of URLs on this repo. xpath() isn't returning raw strings, so we have to
        # convert them first. We also need to strip out all GET parameters if any.
        tree = etree.HTML(resp.content)
        links = frozenset([str(l).split("?")[0] for l in tree.xpath("//a/@href")])
        match, found = False, False
        for link in links:
            # we are going to check for valid changelog links on the root first. We do that by
            # checking if the link ends with one of out changelog filename candidates.
            for candidate in CHANGELOG_FILENAME_CANDIDATES:
                if link.endswith(candidate):
                    if "github.com" in repo_url and "blob" in link:
                        link = link.replace(repo_url, "")
                        match = validate_url("https://raw.githubusercontent.com" + link.replace("/blob/", "/"))
                    elif "bitbucket.org" in repo_url and "src" in link:
                        match = validate_url("https://bitbucket.org" + link.replace("/src/", "/raw/"))
                    elif "sourceforge.net" in repo_url:
                        match = validate_url(repo_url + link + "?format=raw")
                    if match:
                        yield match
                        match, found = False, True

        # if this is a deep search and we haven't found any changelogs on the repo root, we are
        # going to check every potential doc page.
        if deep and not found:
            for link in links:
                sublink = False
                for doc_candidate in DOCS_CANDIDATES:
                    if link.endswith(doc_candidate):
                        if "github.com" in repo_url and "tree" in link:
                            if link.startswith("https://github.com"):
                                sublink = link
                            else:
                                sublink = "https://github.com" + link
                        elif "bitbucket.org" in repo_url and "src" in link:
                            sublink = "https://bitbucket.org" + link
                        # if we find a valid link to a doc subdirectory on the repo call this
                        # function again and yield all possible changelog hits
                        if sublink:
                            for _url in find_changelog(session, sublink, deep=False):
                                yield _url
                                sublink = False


def find_release_page(session, repo_url):
    if "github.com" in repo_url:
        logger.debug("Unable to find changelog on {}, try release page".format(repo_url))
        try:
            username, reponame = repo_url.split("/")[3:5]
            # try to fetch the release page. if it 200s, yield the release page
            # api URL for further processing
            resp = session.get("https://github.com/{username}/{reponame}/releases".format(
                username=username, reponame=reponame
            ))
            if resp.status_code == 200:
                yield "https://api.github.com/repos/{username}/{reponame}/releases".format(
                    username=username, reponame=reponame
                )
        except IndexError:
            logger.debug("Unable to construct releases url for {}".format(repo_url))


def filter_repo_urls(candidates):
    """
    Filters down a list of URL candidates
    :param candidates: list, URL candidates
    :return: set, Repo URLs
    """
    # first, we are going to filter down the URL candidates to be all valid urls
    candidates = set(url for url in [validate_url(_url) for _url in candidates] if url)
    logger.info("Got repo candidates {}".format(candidates))
    repos = set(url for url in [validate_repo_url(_url) for _url in candidates] if url)
    logger.info("Filtered initial candidates down to {}".format(repos))

    return repos


def find_changelogs(session, name, candidates):
    """
    Tries to find changelogs on the given URL candidates
    :param session: requests Session instance
    :param name: str, project name
    :param candidates: list, URL candidates
    :return: tuple, (set(changelog URLs), set(repo URLs))
    """
    repos = filter_repo_urls(candidates=candidates)
    # if we are lucky and there isn't a valid repo URL in our URL candidates, we need to go deeper
    # and check the URLs if they contain a link to a repo
    if not repos:
        logger.info("No repo found, trying to find one on related sites {}".format(candidates))
        repos = set(find_repo_urls(session, name, candidates))

    urls = []
    for repo in repos:
        for url in find_changelog(session, repo):
            urls.append(url)

    if not urls:
        # at this point we failed to fetch a changelog from plain files. we might find one on the
        # github release page.
        logger.debug("No plain changelog urls found, trying release page")
        for repo in repos:
            for url in find_release_page(session, repo):
                urls.append(url)
    return set(urls), repos


def find_git_repo(session, name, candidates):
    """
    Tries to find git repos on the given URL candidates
    :param session: requests Session instance
    :param name: str, project name
    :param candidates: list, URL candidates
    :return: tuple, (set(git URLs), set(repo URLs))
    """

    repos = filter_repo_urls(candidates=candidates)

    # if we are lucky and there isn't a valid repo URL in our URL candidates, we need to go deeper
    # and check the URLs if they contain a link to a repo
    if not repos:
        logger.info("No repo found, trying to find one on related sites {}".format(candidates))
        repos = set(find_repo_urls(session, name, candidates))

    urls = []
    for repo in repos:
        username, reponame = repo.split("/")[3:5]
        if "github.com" in repo:
            urls.append(
                "https://github.com/{username}/{reponame}.git".format(
                    username=username, reponame=reponame
                )
            )
        elif "bitbucket.org" in repo:
            urls.append(
                "https://bitbucket.org/{username}/{reponame}".format(
                    username=username, reponame=reponame
                )
            )
    return set(urls), repos
