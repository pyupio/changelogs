# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


def get_metadata(session, name):
    """
    Gets meta data from pypi for the given package.
    :param session: requests Session instance
    :param name: str, package
    :return: dict, meta data
    """
    resp = session.get("https://rubygems.org/api/v1/gems/{}.json".format(name))
    if resp.status_code == 200:
        return resp.json()
    return {}


def get_releases(data, **kwargs):
    """
    Gets all releases from pypi meta data.
    :param data: dict, meta data
    :return: list, str releases
    """
    if "version" in data:
        return [data["version"], ]
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
    candidates = [
        url for url in
        [data.get(attr) for attr in (
            "project_uri", "homepage_uri", "wiki_uri", "documentation_uri", "mailing_list_uri",
            "source_code_uri", "bug_tracker_uri"
        )]
        if url
    ]
    return set(find_changelogs_fn(session=session, name=name, candidates=candidates))
