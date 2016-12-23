# -*- coding: utf-8 -*-
import re
from packaging.version import Version, InvalidVersion

INVALID_LINE_START = frozenset(["-", "*", " ", "\t", "<!--"])
INVALID_LINE_ENDS = frozenset(["."])
COMMON_RELEASE_INTRODUCTION = frozenset(["release ", "version ", "new in "])


def parse(name, content, releases, get_head_fn):
    """
    Parses the given content for a valid changelog
    :param name: str, package name
    :param content: str, content
    :param releases: list, releases
    :param get_head_fn: function
    :return: dict, changelog
    """
    changelog = {}
    releases = frozenset(releases)
    head = False
    for line in content.splitlines():
        new_head = get_head_fn(name=name, line=line, releases=releases)
        if new_head:
            head = new_head
            changelog[head] = ""
            continue
        if not head:
            continue
        line = line.replace("@", "")
        line = line.replace("#", "")
        changelog[head] += line + "\n"
    return changelog


def get_head(name, line, releases):
    """
    Checks if `line` is a head
    :param name: str, package name
    :param line: str, line
    :param releases: list, releases
    :return: str, version if this is a valid head, False otherwise
    """
    if not line:
        return False
    # if this line begins with an invalid starting character, return early.
    # invalid characters are those used by various markup languages to introduce a new
    # new list item
    for char in INVALID_LINE_START:
        # markdown uses ** for bold text, we also want to make sure to not exclude lines
        # that contain a release
        if line.startswith(char) and not line.startswith("**") and not "release" in line.lower():
            return False
    # if this line ends with a "." this isn't a valid head, return early.
    for char in INVALID_LINE_ENDS:
        if line.endswith(char):
            return False

    # Our goal is to find a somewhat parseable line. For this to work, we need to remove all
    # parts that are not needed so that:
    # release (12/12/2016) v2.0.3
    # becomes something like
    # 12 12 2016 v2.0.3

    # remove all needless clutter from the line, but preserve characters that are used as
    # seperators like "/" and "\".
    line = line.replace("/", " ").replace("\\", " ")
    uncluttered = re.sub("[^0123456789. a-zA-Z]", "", line).strip().lower()

    # we are looking for a valid head here. If the head contains "release" or "version" we are
    # pretty close but don't want them included when we try to parse the version. Remove them.
    for intro in COMMON_RELEASE_INTRODUCTION:
        if uncluttered.startswith(intro):
            uncluttered = uncluttered.replace(intro, "")

    # some projects use the project name as a prefix, remove it
    uncluttered_name = re.sub("[^0123456789. a-zA-Z]", "", name).strip().lower()
    uncluttered = uncluttered.replace(uncluttered_name, "").strip()

    # now that all the clutter is removed, the line should be relatively short. If this is a valid
    # head the only thing left should be the version and possibly some datestamp. We are going
    # to count the length and assume a length of 8 for the version part, 8 for the datestamp and
    # 2 as a safety. Leaving us with a max line length of 18
    #if len(uncluttered) > 40:
    #    return False

    # split the line in parts and sort these parts by "." count in reversed order. This turns a
    # line like "12 12 2016 v2.0.3 into ['v2.0.3', "12", "12", "2016"]
    parts = uncluttered.split(" ")
    if len(parts) > 1:
        parts = parts[::len(parts)-1]
        parts.sort(key=lambda s: s.count("."), reverse=True)

    # loop over all our parts an find a parseable version
    for part in parts:
        # remove the "v" prefix as it is not parseable
        if part.startswith("v"):
            part = part[1:]
        # if there is no "." in this part, continue with the next one
        if "." not in part:
            continue
        # looking good so far, return the version if it is parseable
        try:
            Version(part)
            return part
        except InvalidVersion as e:
            pass
    return False
