"""Custom parser for PyInotify"""

URL = ("https://raw.githubusercontent.com/wiki/seb-m/pyinotify/"
       "Recent-Developments.md")


def get_urls(releases, **kwargs):
    return {URL}, set()
