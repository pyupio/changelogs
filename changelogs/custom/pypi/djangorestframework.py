URL_PREFIX = 'https://raw.githubusercontent.com/tomchristie/django-rest-framework/'


def get_urls(releases, **kwargs):
    return [
        URL_PREFIX + 'master/docs/topics/release-notes.md',
        URL_PREFIX + 'version-2.4.x/docs/topics/release-notes.md'
    ], set()
