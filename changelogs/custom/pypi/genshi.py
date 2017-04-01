"""Custom parser for Genshi"""

URL = "https://genshi.edgewall.org/export/head/trunk/ChangeLog"


def get_urls(releases, **kwargs):
    return {URL}, set()
