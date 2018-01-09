def get_urls(releases, **kwargs):
    return {
        'https://raw.githubusercontent.com/SatelliteQE/robozilla/master/HISTORY'
    }, set()


def get_head(line, releases, **kwargs):
    for release in releases:
        if line.startswith(release) and line.endswith(")"):
            return release
    return False
