def get_urls(releases, **kwargs):
    urls = set()
    for release in releases:
        urls.add(
            'https://raw.githubusercontent.com'
            '/numpy/numpy/master/doc/release/{release}-notes.rst'.format(release=release)
        )
    return urls, set()


def get_head(line, releases, **kwargs):
    # This is the same as SQLAlchemy.
    for release in releases:
        if "NumPy {} Release Notes".format(release) == line:
            return release
    return False
