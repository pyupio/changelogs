from lxml import etree
import sys


def get_urls(releases, **kwargs):
    urls = set()
    for release in releases:
        urls.add(
            'https://docs.newrelic.com/docs/release-notes/agent-release-notes/'
            'python-release-notes/python-agent-{}'.format(release.replace('.', ''))
        )
    return urls, set()


def get_content(session, urls):
    log = ""
    for url in urls:
        r = session.get(url)
        if r.status_code == 200:
            root = etree.HTML(r.content)
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
