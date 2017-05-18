def get_head(line, releases, **kwargs):
    for release in releases:
        if ":release:`{} ".format(release) in line:
            return release
    return False
