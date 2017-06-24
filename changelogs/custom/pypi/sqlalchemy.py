def get_head(line, releases, **kwargs):
    for release in releases:
        if "    :version: {}".format(release) == line:
            return release
    return False


def get_urls(releases, **kwargs):
    # sqlalchemy changelogs are stored as changelog_{major}{minor}.rst
    log_names = set(["".join(r.split('.')[:2]) for r in releases if "beta" not in r])
    # sort urls to make them compatible for testing
    urls = sorted([
        "https://raw.githubusercontent.com/zzzeek/sqlalchemy/master/doc/build/changelog/changelog_{}.rst".format(v) for v in log_names
    ])
    return urls, set()
