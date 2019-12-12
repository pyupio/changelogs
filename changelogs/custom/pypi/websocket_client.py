def get_urls(releases, **kwargs):
    return {
        'https://raw.githubusercontent.com/websocket-client/websocket-client/master/ChangeLog'
    }, set()


def get_head(line, releases, **kwargs):
    for release in releases:
        if "- {}".format(release) == line or "- v{}".format(release) == line:
            return release
    return False
