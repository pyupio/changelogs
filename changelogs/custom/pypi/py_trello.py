URL = 'https://raw.githubusercontent.com/sarumont/py-trello/master/CHANGELOG'


def get_head(line, releases, **kwargs):
    for release in releases:
        print("checking", release, "vs", line)
        if "v{}".format(release) == line:
            return release
    return False


def get_urls(releases, **kwargs):
    return {URL}, set()
