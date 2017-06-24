# -*- coding: utf-8 -*-
import subprocess
from tempfile import mkdtemp
import imp
import requests
import os
import re
from requests import Session
import logging

logger = logging.getLogger(__name__)

ALLOWED_CUSTOM_FUNCTIONS = ("parse", "get_head", "get_urls",
                            "get_content")

GITHUB_API_TOKEN = os.environ.get("CHANGELOGS_GITHUB_API_TOKEN", False)


def _load_custom_functions(vendor, name):
    """
    Loads custom functions from custom/{vendor}/{name}.py. This allows to quickly override any
    function that is used to retrieve and parse the changelog.
    :param name: str, package name
    :param vendor: str, vendor
    :return: dict, functions
    """
    functions = {}
    # Some packages have dash in their name, replace them with underscore
    # E.g. python-ldap to python_ldap
    filename = "{}.py".format(name.replace("-", "_").lower())
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),  # current working dir
        "custom",  # /dir/parser
        vendor,  # /dir/parser/pypi
        filename  # /dir/parser/pypi/django.py
    )
    if os.path.isfile(path):
        module_name = "parser.{vendor}.{name}".format(vendor=vendor, name=name)
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
    elif vendor == "launchpad":
        from . import launchpad
        fns.update({
            "get_metadata": launchpad.get_metadata,
            "get_releases": launchpad.get_releases,
            "get_urls": launchpad.get_urls,
            "find_changelogs": launchpad.find_changelogs,
            "get_content": launchpad.get_content,
            "parse": launchpad.parse
        })

    # load custom functions for special packages lying in custom/{vendor}/{package}.py
    custom_fns = _load_custom_functions(vendor=vendor, name=name)
    fns.update(custom_fns)

    # update custom functions with those passed in here. This allows
    fns.update(functions)
    return fns


def check_for_launchpad(old_vendor, name, urls):
    """Check if the project is hosted on launchpad.

    :param name: str, name of the project
    :param urls: set, urls to check.
    :return: the name of the project on launchpad, or an empty string.
    """
    if old_vendor != "pypi":
        # XXX This might work for other starting vendors
        # XXX but I didn't check. For now only allow
        # XXX pypi -> launchpad.
        return ''

    for url in urls:
        try:
            return re.match(r"https?://launchpad.net/([\w.\-]+)",
                            url).groups()[0]
        except AttributeError:
            continue
    return ''


def check_switch_vendor(old_vendor, name, urls, _depth=0):
    """Check if the project should switch vendors. E.g
    project pushed on pypi, but changelog on launchpad.

    :param name: str, name of the project
    :param urls: set, urls to check.
    :return: tuple, (str(new vendor name), str(new project name))
    """
    if _depth > 3:
        # Protect against recursive things vendors here.
        return ""
    new_name = check_for_launchpad(old_vendor, name, urls)
    if new_name:
        return "launchpad", new_name
    return "", ""


def get(name, vendor="pypi", functions={}, _depth=0):
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
    urls, repos = fns["get_urls"](
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
    del fns
    if changelog:
        return changelog

    # We could not find any changelogs.
    # Check to see if we can switch vendors.
    new_vendor, new_name = check_switch_vendor(vendor, name, repos,
                                               _depth=_depth)
    if new_vendor and new_vendor != vendor:
        return get(new_name, vendor=new_vendor, functions=functions,
                   _depth=_depth+1)
    return {}


def get_commit_log(name, vendor='pypi', functions={}, _depth=0):
    """
    Tries to parse a changelog from the raw commit log.
    :param name: str, package name
    :param vendor: str, vendor
    :param functions: dict, custom functions
    :return: tuple, (dict -> commit log, str -> raw git log)
    """
    if "find_changelogs" not in functions:
        from .finder import find_git_repo
        functions["find_changelogs"] = find_git_repo
    if "get_content" not in functions:
        functions["get_content"] = clone_repo
    if "parse" not in functions:
        from .parser import parse_commit_log
        functions["parse"] = parse_commit_log
    return get(
        name=name,
        vendor=vendor,
        functions=functions
    )


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
            logger.debug("GET changelog from {url}".format(url=url))
            if "https://api.github.com" in url and url.endswith("releases"):
                # this is a github API release page, fetch it if token is set
                if not GITHUB_API_TOKEN:
                    logger.warning("Fetching release pages requires CHANGELOGS_GITHUB_API_TOKEN "
                                   "to be set")
                    continue
                resp = session.get(url, headers={
                    "Authorization": "token {}".format(GITHUB_API_TOKEN)
                })
                if resp.status_code == 200:
                    for item in resp.json():
                        content += "\n\n{}\n{}".format(item['tag_name'], item["body"])
            else:
                resp = session.get(url)
                if resp.status_code == 200:
                    content += "\n\n" + resp.text
        except requests.ConnectionError:
            pass
    return content


def clone_repo(session, urls):
    """
    Clones the given repos in temp directories
    :param session: requests Session instance
    :param urls: list, str URLs
    :return: tuple, (str -> directory, str -> URL)
    """
    repos = []
    for url in urls:
        dir = mkdtemp()
        call = ["git", "clone", url, dir]
        subprocess.call(call)
        repos.append((dir, url))
    return repos
