def get_head(line, releases, **kwargs):
    for release in releases:
        if "Django {} release notes".format(release) in line:
            return release
    return False


def get_urls(releases, **kwargs):
    urls = []
    for release in releases:
        urls.append("https://raw.githubusercontent.com/django/django/master/docs/releases/{v}.txt".format(v=release))
    return urls, []
