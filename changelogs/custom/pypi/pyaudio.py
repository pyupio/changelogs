import re

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")
URL = ("https://people.csail.mit.edu/hubert/git/?"
       "p=pyaudio.git;a=blob_plain;f=CHANGELOG;hb=HEAD")


def get_urls(releases, **kwargs):
    return {URL}, set()


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
    date_line = None
    for line in content.splitlines():
        if DATE_RE.match(line):
            date_line = line
            continue
        if line.strip().startswith("PyAudio"):
            try:
                head = line.strip().split()[1]
            except:
                continue
            changelog[head] = date_line + "\n"
            continue
        if not head:
            continue
        line = line.replace("@", "")
        line = line.replace("#", "")
        changelog[head] += line + "\n"
    return changelog