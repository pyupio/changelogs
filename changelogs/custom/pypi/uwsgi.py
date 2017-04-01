import requests


def get_urls(releases, **kwargs):
    # sort urls to make them compatible for testing
    urls = sorted([
        "https://raw.githubusercontent.com/unbit/uwsgi-docs/master/Changelog"
        "-{}.rst".format(v) for v in releases
    ])
    return urls, set()


def get_content(session, urls):
    content = {}
    for url in urls:
        v = url.rsplit("-", 1)[1].rsplit(".", 1)[0]
        try:
            resp = session.get(url)
            if resp.status_code == 200:
                content[v] = resp.text.split("\n", 2)[-1]
        except requests.ConnectionError:
            pass
    return content


def parse(name, content, releases, get_head_fn):
    return content