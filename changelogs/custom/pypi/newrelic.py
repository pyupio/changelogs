from lxml import etree
from changelogs.changelogs import get_limited_content_entry
import sys


def get_urls(releases, **kwargs):
    urls = set()
    for release in releases:
        urls.add(
            'https://docs.newrelic.com/docs/release-notes/agent-release-notes/'
            'python-release-notes/python-agent-{}'.format(release.replace('.', ''))
        )
    return urls, set()


def get_content(session, urls, chars_limit):
    log = ""
    for url in urls:
        limited_content_entry = get_limited_content_entry(session, url, chars_limit)
        if limited_content_entry:
            root = etree.HTML(limited_content_entry)
        else:
            continue
        try:
            article = root.xpath("//article/div[@class='content']")[0]
            content = etree.tostring(article, method="text", encoding='utf-8')
            if sys.version_info > (3, 0):
                content = content.decode("utf-8")
            # remove first two lines
            content = '\n'.join(content.split('\n')[2:-1])
            log += "# {version}\n{content}\n\n".format(
                version=url.split("-")[-1],
                content=content,
                )
        except IndexError:
            pass
    return log


def get_head(line, releases, **kwargs):
    for release in releases:
        if "# {}".format(release.replace(".", "")) == line:
            return release
    return False
