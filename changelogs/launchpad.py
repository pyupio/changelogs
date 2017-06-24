# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


def get_metadata(session, name):
    """
    Gets meta data from launchpad for the given package.
    :param session: requests Session instance
    :param name: str, package
    :return: dict, meta data
    """
    resp = session.get(
        "https://api.launchpad.net/1.0/{}/releases".format(name))
    if resp.status_code == 200:
        return resp.json()
    return {}


def get_releases(data, **kwargs):
    """
    Gets all releases from pypi meta data.
    :param data: dict, meta data
    :return: list, str releases
    """
    if "entries" in data:
        return [e["version"] for e in data["entries"]]
    return []


def find_changelogs(session, name, candidates):
    """
    Tries to find changelogs on the given URL candidates
    :param session: requests Session instance
    :param name: str, project name
    :param candidates: list, URL candidates
    :return: tuple, (set(changelog URLs), set(repo URLs))
    """
    return set(), set()


def get_urls(session, name, data, find_changelogs_fn, **kwargs):
    """
    Gets URLs to changelogs.
    :param session: requests Session instance
    :param name: str, package name
    :param data: dict, meta data
    :param find_changelogs_fn: function, find_changelogs
    :return: tuple, (set(changelog URLs), set(repo URLs))
    """
    # if this package has valid meta data, build up a list of URL candidates we can possibly
    # search for changelogs on
    return {"https://api.launchpad.net/1.0/{}/releases".format(name)}, set()


def get_content(session, urls):
    """
    Loads the content from URLs, ignoring connection errors.
    :param session: requests Session instance
    :param urls: list, str URLs
    :return: str, content
    """
    for url in urls:
        resp = session.get(url)
        if resp.ok:
            return resp.json()
    return {}


def parse(name, content, releases, get_head_fn):
    """
    Parses the given content for a valid changelog
    :param name: str, package name
    :param content: str, content
    :param releases: list, releases
    :param get_head_fn: function
    :return: dict, changelog
    """
    try:
        return {e["version"]: e["changelog"] for e in content["entries"]
                if e["changelog"]}
    except KeyError:
        return {}
