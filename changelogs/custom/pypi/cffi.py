import requests
from lxml import etree


def get_urls(releases, **kwargs):
    urls = set()
    # unable to link to latest on bitbucket. have to scrape the URL
    r = requests.get(
        'https://bitbucket.org/cffi/release-doc/src/default/doc/source/whatsnew.rst' +
        '?fileviewer=file-view-default')
    if r.status_code == 200:
        tree = etree.HTML(r.content)
        # find the link that ends with whatsnew.txt
        for link in frozenset([str(href).split("?")[0] for href in tree.xpath("//a/@href")]):
            if link.endswith("whatsnew.rst") and "/raw/" in link:
                urls.add("https://bitbucket.org" + link)
    return urls, set()
