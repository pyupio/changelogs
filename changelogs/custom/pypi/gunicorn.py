from datetime import datetime

def get_urls(releases, **kwargs):
    # gunicorn uses {year}-news.rst
    urls = [
        "https://raw.githubusercontent.com/benoitc/gunicorn/master/docs/source/{}-news.rst"
            .format(year) for year in range(2010, datetime.now().year + 1)
    ]
    print(urls)
    return urls, set()
