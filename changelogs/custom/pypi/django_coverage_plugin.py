def get_urls(releases, **kwargs):
    return {
        'https://raw.githubusercontent.com/nedbat/django_coverage_plugin/master/README.rst'
    }, set()


def get_head(line, releases, **kwargs):
    for release in releases:
        if "v{} --- ".format(release) in line:
            return release
    return False
