"""Custom parser for IMAPClient"""

URL = ("https://raw.githubusercontent.com/mjs/imapclient/master/doc/src"
       "/releases.rst")


def get_head(name, line, releases):
    if not line.strip().startswith("Version"):
        return False

    return line.strip().rsplit(None, 1)[1]

def get_urls(releases, **kwargs):
    return {URL}, set()
