from __future__ import unicode_literals


def get_urls(releases, **kwargs):
    return {
        'https://alabaster.readthedocs.io/en/latest/_sources/changelog.rst.txt'
    }, set()


def get_head(line, releases, **kwargs):
    for release in releases:
        if ":release:`{}".format(release) in line:
            return release
    return False
