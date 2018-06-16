import re

def get_urls(releases, **kwargs):
    return {
        'https://raw.githubusercontent.com/DemocracyClub/uk-election-ids/master/CHANGELOG.md'
    }, set()

def get_head(line, releases, **kwargs):
    for release in releases:
        pattern = re.compile(r"## :package: [[]?{}[]]?.+".format(release))
        if pattern.match(line):
            return release
    return False
