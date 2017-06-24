"""Custom parser for python-ldap"""

URL = ("http://python-ldap.cvs.sourceforge.net/viewvc/python-ldap/python-ldap"
       "/CHANGES")


def get_urls(releases, **kwargs):
    return {URL}, set()
