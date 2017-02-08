def get_urls(releases, **kwargs):
    urls = []
    for release in releases:
        # releases like 0.6 are actually saved as 0.6.0.
        if len(release.split('.')) == 2:
            release += '.0'
        urls.append(
            "https://gitlab.com/pycqa/flake8/raw/master/docs/source/release-notes/{v}.rst"
            .format(v=release)
        )
    return urls, []
