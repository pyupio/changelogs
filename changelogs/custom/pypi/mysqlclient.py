"""Custom parsing for mysqlclient."""


def get_head(name, line, releases):
    if not line.strip().startswith("What's new in"):
        return False

    return line.strip().rsplit(None, 1)[1]
