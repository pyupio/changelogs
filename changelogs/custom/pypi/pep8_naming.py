def get_urls(releases, **kwargs):
    return {
        'https://raw.githubusercontent.com/PyCQA/pep8-naming/master/CHANGELOG.rst'
    }, set()


def get_head(line, releases, **kwargs):
    for release in releases:
        if "{} - ".format(release) in line:
            return release
    return False
