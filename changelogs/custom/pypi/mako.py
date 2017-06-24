"""Custom parser for alembic"""

# Alembic already has a changelog in
# https://bitbucket.org/zzzeek/mako/raw/master/CHANGES
# But the content just says that it moved to this location.
URL = "https://bitbucket.org/zzzeek/mako/raw/master/doc/build/changelog.rst"


def get_head(line, releases, **kwargs):
    # This is the same as SQLAlchemy.
    for release in releases:
        if "    :version: {}".format(release) == line:
            return release
    return False


def get_urls(releases, **kwargs):
    return {URL}, set()
