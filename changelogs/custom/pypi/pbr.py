from __future__ import unicode_literals
from lxml import etree


def get_urls(releases, **kwargs):
    return {
        'https://docs.openstack.org/developer/pbr/history.html'
    }, set()


def get_content(session, urls):
    log = ""
    for url in urls:
        r = session.get(url)
        if r.status_code == 200:
            root = etree.HTML(r.content)
            for item in root.xpath("//div[@class='section']"):
                try:
                    log += "{version}\n{content}\n\n".format(
                        version=item.xpath("h3/text()")[0],
                        content="\n".join(["- {}".format(li) for li in item.xpath("ul/li/text()")])
                    )
                except IndexError:
                    pass
    return log
