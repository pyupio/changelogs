"""Custom parsing for mysqlclient."""


def get_head(name, line, releases):
    """Parses content from:

    https://github.com/PyMySQL/mysqlclient-python/blob/master/HISTORY.md

    Each HEAD line looks like:

        What's new in 1.3.10

    """
    if not line.strip().startswith("What's new in"):
        return False

    return line.strip().rsplit(None, 1)[1]
