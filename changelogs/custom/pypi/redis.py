"""Custom parser for redis"""


def get_head(name, line, releases):
    if not line.startswith("* "):
        return False
    try:
        return line.split()[1]
    except IndexError:
        return False