def get_urls(releases, **kwargs):
    return {
        'https://raw.githubusercontent.com/brack3t/django-braces/master/docs/changelog.rst'
    }, set()


def get_head(line, releases, **kwargs):
    for release in releases:
        if "* :release:`{}".format(release) in line:
            return release
    return False
