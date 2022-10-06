from __future__ import unicode_literals
from lxml import etree
from changelogs.changelogs import get_limited_content_entry


def get_urls(releases, **kwargs):
    return {
        'https://docs.openstack.org/developer/pbr/history.html'
    }, set()


def get_content(session, urls, chars_limit):
    log = ""
    for url in urls:
        limited_content_entry = get_limited_content_entry(session, url, chars_limit)
        if limited_content_entry:
            root = etree.HTML(limited_content_entry)
        else:
            continue
        for item in root.xpath("//div[@class='section']"):
            try:
                log += "{version}\n{content}\n\n".format(
                    version=item.xpath("h3/text()")[0],
                    content="\n".join(["- {}".format(li) for li in item.xpath("ul/li/text()")])
                    )
            except IndexError:
                pass
    return log
