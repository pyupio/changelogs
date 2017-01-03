def get_urls(releases, **kwargs):
    urls = []
    for release in releases:
        if release == "2.0":
            release = "2.0.0"
        urls.append("https://raw.githubusercontent.com/boto/boto/develop/docs/source/releasenotes/v{v}.rst".format(v=release))
    return urls, []
