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
    resp = session.get("https://registry.npmjs.org/{}".format(name))
    if resp.status_code == 200:
        return resp.json()
    return {}


def get_releases(data, **kwargs):
    """
    Gets all releases from pypi meta data.
    :param data: dict, meta data
    :return: list, str releases
    """
    if "versions" in data:
        return sorted(data["versions"].keys(), key=lambda v: parse(v), reverse=True)
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
    if "versions" in data:
        candidates = set()
        for version, item in data["versions"].items():
            if "homepage" in item:
                candidates.add(item["homepage"])
            if "repository" in item:
                repo = item["repository"]["url"]
                repo = repo.replace("git://", "https://").replace(".git", "")
                candidates.add(repo)
        return set(find_changelogs_fn(session=session, name=name, candidates=candidates))
    return set()
