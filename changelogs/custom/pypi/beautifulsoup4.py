# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import requests
from lxml import etree


def get_urls(releases, **kwargs):
    # changelog is on launchpad.
    r = requests.get('https://bazaar.launchpad.net/~leonardr/beautifulsoup/bs4/view/head:/CHANGELOG')
    root = etree.HTML(r.text)
    link = root.xpath("//a[contains(text(),'download file')]/@href")[0]
    return ["https://bazaar.launchpad.net" + link], set()
