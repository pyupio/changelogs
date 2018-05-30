import logging
import sys

from lxml import etree


CHANGELOG = ('https://github.com/HypothesisWorks/hypothesis/blob/master/'
             'hypothesis-python/docs/changes.rst')

logger = logging.getLogger(__name__)


def get_urls(*args, **kwargs):
    return {CHANGELOG}, set()


def get_content(session, urls):
    def get_element_body(e):
        if e.tag in {'ul', 'ol'}:
            return '\n'.join('- {}'.format(get_element_body(x)) for x in e)
        e = etree.tostring(e, method='text', encoding='utf-8').strip()
        e = e.decode('utf-8') if sys.version_info[0] >= 3 else e
        return e.replace('\n', ' ')

    log = ''
    for url in urls:
        try:
            r = session.get(url)
            r.raise_for_status()
        except Exception:
            logger.warning('error retrieving changelog')
            return ''

        root = etree.HTML(r.content)
        for release in root.xpath('//h2'):
            header = get_element_body(release)
            version = header.split(' - ')[0].strip(',')

            contents = []
            itt = release.getnext()
            while itt is not None and itt.tag != 'h2':
                contents.append(get_element_body(itt))
                itt = itt.getnext()

            log += '# {version}\n{contents}\n\n'.format(
                version=version,
                contents='\n'.join(c for c in contents if c))

    return log
