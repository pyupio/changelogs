def get_urls(releases, **kwargs):
    urls = set()
    for release in releases:
        urls.add(
            'https://raw.githubusercontent.com'
            '/pandas-dev/pandas/master/doc/source/whatsnew/v{release}.txt'.format(release=release)
        )
    return urls, set()


def get_head(line, releases, **kwargs):
    for release in releases:
        if "v{} (".format(release) in line or "v.{} (".format(release) in line:
            return release
    return False
