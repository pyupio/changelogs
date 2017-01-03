# -*- coding: utf-8 -*-
import os
import imp
import requests
import os
from requests import Session
import logging

logger = logging.getLogger(__name__)

ALLOWED_CUSTOM_FUNCTIONS = ("parse", "get_head", "get_urls",)


def _load_custom_functions(vendor, name):
    """
    Loads custom functions from custom/{vendor}/{name}.py. This allows to quickly override any
    function that is used to retrieve and parse the changelog.
    :param name: str, package name
    :param vendor: str, vendor
    :return: dict, functions
    """
    functions = {}
    filename = "{}.py".format(name)
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),  # current working dir
        "custom",  # /dir/parser
        vendor,  # /dir/parser/pypi
        filename  # /dir/parser/pypi/django.py
    )
    if os.path.isfile(path):
        module_name = "{parser}.{vendor}.{name}"
        module = imp.load_source(module_name, path)
        functions = dict(
            (function, getattr(module, function, None)) for function in ALLOWED_CUSTOM_FUNCTIONS
            if hasattr(module, function)
        )
    return functions


def _bootstrap_functions(name, vendor, functions):
    """
    Loads all functions, including custom functions, for the given package/vendor and updates it
    with the functions passed to this function. [:)]
    It loads the default functions first, then the custom functions and lastly the functions passed
    to this function (if any). [:)]
    :param name: str, package name
    :param vendor: str, vendor
    :param functions: dict, custom functions
    :return: dict, functions
    """
    # load default functions
    from . import parser
    from . import finder
    fns = {
        "get_content": get_content,
        "parse": parser.parse,
        "get_head": parser.get_head,
        "find_changelogs": finder.find_changelogs
    }

    # load vendor functions
    if vendor == "pypi":
        from . import pypi
        fns.update({
            "get_metadata": pypi.get_metadata,
            "get_releases": pypi.get_releases,
            "get_urls": pypi.get_urls,
        })
    elif vendor == "npm":
        from . import npm
        fns.update({
            "get_metadata": npm.get_metadata,
            "get_releases": npm.get_releases,
            "get_urls": npm.get_urls,
        })
    elif vendor == "gem":
        from . import rubygems
        fns.update({
            "get_metadata": rubygems.get_metadata,
            "get_releases": rubygems.get_releases,
            "get_urls": rubygems.get_urls,
        })

    # load custom functions for special packages lying in custom/{vendor}/{package}.py
    custom_fns = _load_custom_functions(vendor=vendor, name=name)
    fns.update(custom_fns)

    # update custom functions with those passed in here. This allows
    fns.update(functions)
    return fns


def get(name, vendor="pypi", functions={}):
    """
    Tries to find a changelog for the given package.
    :param name: str, package name
    :param vendor: str, vendor
    :param functions: dict, custom functions
    :return: dict, changelog
    """
    fns = _bootstrap_functions(name=name, vendor=vendor, functions=functions)
    session = Session()
    # get meta data for the given package and use this metadata to
    # find urls pointing to a possible changelog
    data = fns["get_metadata"](session=session, name=name)
    releases = fns["get_releases"](name=name, data=data)
    urls = fns["get_urls"](
        session=session,
        name=name,
        data=data,
        releases=releases,
        find_changelogs_fn=fns["find_changelogs"]
    )

    # load the content from the given urls and parse the changelog
    content = fns["get_content"](session=session, urls=urls)
    changelog = fns["parse"](
        name=name,
        content=content,
        releases=releases,
        get_head_fn=fns["get_head"]
    )
    return changelog


def get_content(session, urls):
    """
    Loads the content from URLs, ignoring connection errors.
    :param session: requests Session instance
    :param urls: list, str URLs
    :return: str, content
    """

    content = ""
    for url in urls:
        try:
            resp = session.get(url)
            logger.info("GET changelog from {url}".format(url=url))
            if resp.status_code == 200:
                content += "\n\n" + resp.text
        except requests.ConnectionError:
            pass
    return content
