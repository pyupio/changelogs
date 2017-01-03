# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from packaging.version import parse


def get_metadata(session, name):
    """
    Gets meta data from pypi for the given package.
    :param session: requests Session instance
    :param name: str, package
    :return: dict, meta data
    """
    resp = session.get("https://pypi.python.org/pypi/{}/json".format(name))
    if resp.status_code == 200:
        return resp.json()
    return {}


def get_releases(data, **kwargs):
    """
    Gets all releases from pypi meta data.
    :param data: dict, meta data
    :return: list, str releases
    """
    if "releases" in data:
        return sorted(data["releases"].keys(), key=lambda v: parse(v), reverse=True)
    return []


def get_urls(session, name, data, find_changelogs_fn, **kwargs):
    """
    Gets URLs to changelogs.
    :param session: requests Session instance
    :param name: str, package name
    :param data: dict, meta data
    :param find_changelogs_fn: function, find_changelogs
    :return: set, URLs to changelogs
    """
    # if this package has valid meta data, build up a list of URL candidates we can possibly
    # search for changelogs on
    if "info" in data:
        # add all URLs in pypi's meta data:
        # {
        #   "info": {
        #       "home_page":
        #       "docs_url":
        #       "bugtrack_url":
        #   }
        # }
        candidates = [
            url for url in
            [data["info"].get(attr) for attr in ("home_page", "docs_url", "bugtrack_url")]
            if url
        ]
        # the latest release page on pypi might also contain links, add it
        candidates.append("https://pypi.python.org/pypi/{name}/{latest_release}".format(
            name=name,
            latest_release=next(iter(get_releases(data)))
        ))
        return set(find_changelogs_fn(session=session, name=name, candidates=candidates))
    return set()
