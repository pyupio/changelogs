def get_urls(releases, **kwargs):
    return {'https://raw.githubusercontent.com/PyCQA/mccabe/master/README.rst'}, set()


def get_head(line, releases, **kwargs):
    for release in releases:
        if "{} - ".format(release) in line:
            return release
    return False
