#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
import changelogs

"""
bcryptor
zopyx.txng3.core
"""


@pytest.fixture(autouse=True)
@pytest.mark.usefixtures('betamax_session')
def record(monkeypatch, betamax_session):
    def session():
        return betamax_session
    monkeypatch.setattr("changelogs.changelogs.Session", session)


def test_bundler():
    log = changelogs.get("bundler", vendor="gem")
    assert "method public again, fixing a regression in 1.13.4" in log["1.13.6"]
    assert "Fix cross repository dependencies" in log["1.1.pre.6"]
    assert "Rubinius platform :rbx" in log["1.0.14"]
    assert "Significantly increase performance of resolver" in log["1.0.6"]
    assert "added support for :path" in log["0.9.5"]


def test_babel():
    log = changelogs.get("babel", vendor="npm")
    assert "babel-helper-builder-react-jsx" in log["6.21.1"]
    assert "Exposes raw mappings when source map generation is enabled" in log["6.21.0"]
    assert "Speeeeeeed" in log["5.3.0"]
    assert "6to5 is now known as Babel" in log["4.0.0"]


def test_boto():
    log = changelogs.get("boto")
    assert "Fix connection pooling bug: don't close before reading" in log["2.0"]
    assert "The 2.2.1 release fixes a packaging problem" in log["2.2.1"]
    assert "There were 240 commits made by 34 different authors" in log["2.9.0"]
    assert "Altered the S3 key buffer to be a configurable value" in log["2.9.5"]
    assert "boto.dynamodb2.table.Table" in log["2.43.0"]


def test_django():
    log = changelogs.get("django")
    assert "Welcome to Django 1.1.2!" in log["1.1.2"]
    assert "same template will work with Django 1.2." in log["1.1.2"]


def test_python_amazon_product_api():
    log = changelogs.get("python-amazon-product-api")
    assert "Small bugfix release" in log["0.2.7"]
    assert "def minidom_response_parser(fp)" in log["0.2.3"]
    assert "Initial release." in log["0.1"]
    assert "Support for Python 2.4 added" in log["0.2.1"]


def test_pillow():
    log = changelogs.get("pillow")
    assert "PyPy: Buffer interface workaround" in log["3.5.0"]
    assert "Fix fix for map.c overflow" in log["3.4.1"]
    assert "Added debug option for setup.py to trace header and library finding" in log["3.3.0"]
    assert "Fixed an integer overflow in Jpeg2KEncode.c" in log["3.1.2"]
    assert "Skip any number extraneous chars" in log["3.0.0"]
    assert 'Added a full set of "I" decoders.' in log["0.3b1"]


def test_requests():
    log = changelogs.get("requests")
    assert "- Use simplejson if available." in log["0.13.3"]
    assert "- Sign querystring parameters in OAuth 1.0" in log["0.13.2"]
    assert "Resolve regression introduced" in log["2.9.1"]


def test_argparse():
    log = changelogs.get("argparse")
    assert "argparse cannot handle empty arguments" in log["1.4.1"]
    assert "host the files on pypi" in log["1.2.2"]
    assert "under same license as py 2.7 stdlib argparse code" in log["1.2"]


def test_simplejson():
    log = changelogs.get("simplejson")
    assert "* Better Python 2.5 compatibility" in log["1.5"]
    assert "Documentation updates" in log["3.6.3"]


def test_django_toolkit():
    log = changelogs.get("django-toolkit")
    assert "- Added QuerySetManagerTestCase and" in log["0.2.1"]
    assert "Ensured templates are included in installation." in log["0.3.2"]


def test_amplecode():
    log = changelogs.get("amplecode.recipe.template")
    assert "* Stripping all options before supplying to the templates" in log["0.1.1"]
    assert "All necessary subdirectories are created for the target files" in log["1.2"]


def test_fake_factory():
    log = changelogs.get("fake-factory")

    assert "@michaelcho" not in log["0.5.4"]
    assert "michaelcho" in log["0.5.4"]


def test_dateutil():
    log = changelogs.get("python-dateutil")

    assert "#40" not in log["2.5.0"]
    assert "40" in log["2.5.0"]


def test_pysandbox():
    log = changelogs.get("pysandbox")
    assert "This version is much more functional" in log["1.5"]


def test_mayavi():
    log = changelogs.get("mayavi")
    assert "01 Aug 2016" in log["4.5.0"]


def test_foolscap():
    log = changelogs.get("foolscap")
    assert "Tubs have been using the" in log["0.12.4"]


def test_htmllib():
    log = changelogs.get("html5lib")
    assert "Fix attribute order going to the tree builder" in log["0.999999999"]


def test_115wangpan():
    log = changelogs.get("115wangpan")
    assert "- Initial release." in log["0.1.0"]
    assert "- Fixed broken sdist" in log["0.1.1"]
    assert "- Added download fea" in log["0.2.0"]
    assert "- Fixed ``Task.statu" in log["0.2.1"]
    assert "- Added system depen" in log["0.2.2"]
    assert "- Fixed 2: ``show_pr" in log["0.2.3"]
    assert "- Fixed 5: add isatt" in log["0.2.4"]


def test_17monip():
    log = changelogs.get("17monip")
    assert "First release." in log["0.1.0"]
    assert "Released on June 4, " in log["0.2.0"]
    assert "Released on July 4, " in log["0.2.1"]
    assert "Released on August 5" in log["0.2.2"]
    assert "Released on August 6" in log["0.2.3"]
    assert "Released on November" in log["0.2.4"]
    assert "Released on April 21" in log["0.2.5"]


def test_1pass():
    log = changelogs.get("1pass")
    assert "* Handle padding pro" in log["0.1.5"]
    assert "* Support non-webfor" in log["0.1.6"]
    assert "* Added support for " in log["0.1.7"]
    assert "* Added support for " in log["0.1.8"]
    assert "* Added support for " in log["0.2.0"]
    assert "* Fix pbkdf2 overflo" in log["0.2.1"]


def test_1to001():
    log = changelogs.get("1to001")
    assert "* make basic package" in log["0.1.0"]
    assert "+ add Wheel format t" in log["0.2.0"]
    assert "* fix requirement of" in log["0.2.1"]
    assert "* add ``COPYING`` li" in log["0.3.0"]


def test_3xsd():
    log = changelogs.get("3xsd")
    assert "added:" in log["0.0.16"]
    assert "fixed:" in log["0.0.17"]
    assert "fixed:" in log["0.0.18"]
    assert "unfixed:" in log["0.0.19"]
    assert "fixed:" in log["0.0.20"]
    assert "optimized:" in log["0.0.21"]
    assert "added:" in log["0.0.22"]


def test_a2svm():
    log = changelogs.get("a2svm")
    assert "* Initial release" in log["0.0.1"]
    assert "* modify macro base " in log["0.0.2"]
    assert "* List command is no" in log["0.0.3"]
    assert "* make command is no" in log["0.0.4"]
    assert "* add compatibility " in log["0.0.5"]


def test_aacgmv2():
    log = changelogs.get("aacgmv2")
    assert "* Initial release" in log["1.0.0"]
    assert "* No code changes, d" in log["1.0.10"]
    assert "* Fix bug in subsola" in log["1.0.11"]
    assert "* Return nan in forb" in log["1.0.12"]
    assert "* Correctly convert " in log["1.0.13"]
    assert "* Change method of c" in log["2.0.0"]


def test_aadict():
    log = changelogs.get("aadict")
    assert "* First tagged relea" in log["0.2.1"]
    assert "* Removed `distribut" in log["0.2.2"]
    assert "* Made `clear()` met" in log["0.2.3"]


def test_aartfaac_arthur():
    log = changelogs.get("aartfaac_arthur")
    assert "* fixed problems wit" in log["0.3"]


def test_abbyy():
    log = changelogs.get("abbyy")
    assert "* Initial release" in log["0.1"]
    assert "* Minor fixes" in log["0.2"]
    assert "* Port to Python 3 (" in log["0.3"]


def test_abclinuxuapi():
    log = changelogs.get("abclinuxuapi")
    assert "- Created." in log["0.1.0"]
    assert "- Added a lot of fea" in log["0.2.0"]
    assert "- Added parsing of c" in log["0.3.0"]
    assert "- Added badges to RE" in log["0.4.0"]
    assert "- Added banlist for " in log["0.4.11"]


def test_abcpmc():
    log = changelogs.get("abcpmc")
    assert "* First release" in log["0.1.0"]
    assert "* Python 3 support" in log["0.1.1"]
    assert "* Added support for " in log["0.1.2"]


def test_abe():
    log = changelogs.get("abe")
    assert "* Add support for Bi" in log["0.8"]


def test_abilian_core():
    log = changelogs.get("abilian_core")
    assert "- Initial release." in log["0.1"]
    assert "- Redesigned indexin" in log["0.1.1"]
    assert "- added jinja extens" in log["0.1.2"]
    assert "- Update some depend" in log["0.1.3"]
    assert "- refactored abilian" in log["0.1.4"]
    assert "- Too long to list." in log["0.2.0"]
    assert "Features" in log["0.3.0"]


def test_abilian_sbe():
    log = changelogs.get("abilian_sbe")
    assert "Initial release" in log["0.1"]
    assert "Improvements" in log["0.1.1"]
    assert "- forum reply by mai" in log["0.1.10"]
    assert "Improvements" in log["0.1.2"]
    assert "- Various CSS and HT" in log["0.1.3"]
    assert "- Members: export li" in log["0.1.5"]


def test_ablog_api():
    log = changelogs.get("ablog_api")
    assert "- init" in log["0.0.1"]
    assert "first version cf rea" in log["0.1.0"]
    assert "correction from dev " in log["0.2.0"]
    assert "change manage edit (" in log["0.3.0"]
    assert "change manage get (b" in log["0.4.0"]
    assert "add python version" in log["0.5.0"]
    assert "correction of python" in log["0.5.1"]


def test_ablog_cli():
    log = changelogs.get("ablog_cli")
    assert "- init" in log["0.0.1"]
    assert "First version with v" in log["0.1.0"]
    assert "correction of import" in log["0.3.0"]
    assert "correction of import" in log["0.4.0"]
    assert "change edit and new," in log["0.5.0"]
    assert "change edit and cat:" in log["0.6.0"]
    assert "add python version" in log["0.7.0"]


def test_abraxas():
    log = changelogs.get("abraxas")
    assert "* Changed the name t" in log["1.6"]
    assert "* Replaced Zenity as" in log["1.7"]


def test_abydos():
    log = changelogs.get("abydos")
    assert "- First Beta release" in log["0.1.1"]
    assert "- Added Caumanns' Ge" in log["0.2.0"]


def test_accept():
    log = changelogs.get("accept")
    assert "* Initial Release!" in log["0.1.0"]


def test_accloudtant():
    log = changelogs.get("accloudtant")
    assert "Added" in log["0.1.1"]
    assert "Fixed" in log["0.1.2"]
    assert "Fixed" in log["0.1.3"]


def test_acdcli():
    log = changelogs.get("acdcli")
    assert "new:" in log["0.1.2"]
    assert "* plugin mechanism a" in log["0.1.3"]


def test_ace():
    log = changelogs.get("ace")
    assert "- Fixed too large of" in log["0.3"]


def test_acidfile():
    log = changelogs.get("acidfile")
    assert "* Initial developmen" in log["0.0.1"]
    assert "* First stable relea" in log["1.0.0"]
    assert "+ Python 3 support." in log["1.1.0"]
    assert "+ Python 2.6 support" in log["1.2.0"]
    assert "* Using io.open in s" in log["1.2.1"]


def test_acli():
    log = changelogs.get("acli")
    assert "- Allow use of ls in" in log["0.1.17"]
    assert "- Add initial suppor" in log["0.1.18"]
    assert "- Added ability to d" in log["0.1.20"]
    assert "- Show instance coun" in log["0.1.21"]
    assert "- Make it work with " in log["0.1.23"]
    assert "- Improve permission" in log["0.1.24"]
    assert "- Correct ec2 instan" in log["0.1.25"]


def test_acorn():
    log = changelogs.get("acorn")
    assert "- Fixed streamlining" in log["0.0.10"]
    assert "- Added two extra ig" in log["0.0.11"]
    assert "- Fixed `pandas.get`" in log["0.0.12"]
    assert "- Fixed issue 14." in log["0.0.13"]
    assert "- Added severly rest" in log["0.0.3"]
    assert "- Debugged unit test" in log["0.0.4"]
    assert "- Debugged all unit " in log["0.0.5"]


def test_acp_calendar():
    log = changelogs.get("acp_calendar")
    assert "* First release on P" in log["0.2.2"]


def test_acquisition():
    log = changelogs.get("acquisition")
    assert "- Release as separat" in log["2.12"]
    assert "- Update for iterati" in log["2.12.1"]
    assert "- Fixed 64-bit compa" in log["2.12.2"]
    assert "- More 64-bit fixes " in log["2.12.3"]
    assert "- Fix iteration prox" in log["2.12.4"]
    assert "- Added support for " in log["2.13.0"]
    assert "- Update to include " in log["2.13.1"]


def test_acrylamid():
    log = changelogs.get("acrylamid")
    assert "Initial release." in log["0.1"]
    assert "- add static page su" in log["0.2"]
    assert "Released on April, 1" in log["0.3.0"]
    assert "- new content filter" in log["0.3.1"]
    assert "- use a single, comp" in log["0.3.2"]
    assert "- new sitemap genera" in log["0.3.3"]
    assert "- per entry settings" in log["0.3.4"]


def test_acsone_recipe_odoo_pydev():
    log = changelogs.get("acsone_recipe_odoo_pydev")
    assert "- First release" in log["1.0"]
    assert "- `github 1 <https:/" in log["1.1"]
    assert "- `github 4 <https:/" in log["1.2"]
    assert "- `github 5 <https:/" in log["2.0"]


def test_actdiag():
    log = changelogs.get("actdiag")
    assert "* First release" in log["0.1.0"]
    assert "* Fix bugs" in log["0.1.1"]
    assert "* Fix bugs" in log["0.1.2"]
    assert "* Fix bugs" in log["0.1.3"]
    assert "* Change license to " in log["0.1.4"]
    assert "* Fix bugs" in log["0.1.5"]
    assert "* Support input from" in log["0.1.6"]


def test_activecampaign():
    log = changelogs.get("activecampaign")
    assert "* First release on P" in log["0.1.0"]


def test_activity_feed():
    log = changelogs.get("activity_feed")
    assert "- Refactor package l" in log["2.5.4"]


def test_activity_monitor():
    log = changelogs.get("activity_monitor")
    assert "* Decrufted very old" in log["0.1"]
    assert "* Added paginate by " in log["0.10.0"]
    assert "* Small change to ke" in log["0.10.1"]
    assert "* Passing back next " in log["0.10.2"]
    assert "* Passing back next " in log["0.10.3"]
    assert "* Corrected view nex" in log["0.10.5"]


def test_activityio():
    log = changelogs.get("activityio")
    assert "+ Alpha version rele" in log["0.0.1"]
    assert "+ Support added for " in log["0.0.2"]



def test_aio_manager():
    log = changelogs.get("aio_manager")
    assert "Released on April 15" in log["0.1"]
    assert "Released on April 16" in log["0.1.1"]
    assert "Released on April 19" in log["0.1.2"]


def test_aio_periodic():
    log = changelogs.get("aio_periodic")
    assert "- update the status " in log["0.1.4"]
    assert "- update procotol na" in log["0.1.5"]
    assert "- update procotol ad" in log["0.1.6"]


def test_aio_pybars():
    log = changelogs.get("aio_pybars")
    assert "Released on April 19" in log["0.1.0"]


def test_aio_yamlconfig():
    log = changelogs.get("aio_yamlconfig")
    assert "Released on April 19" in log["0.1.0"]
    assert "Released on April 19" in log["0.1.1"]


def test_aioamqp():
    log = changelogs.get("aioamqp")
    assert "* First public previ" in log["0.1"]
    assert "* Add `no_wait` and " in log["0.1.1"]
    assert "* Remove the `asynci" in log["0.2.0"]


def test_aiobotocore():
    log = changelogs.get("aiobotocore")
    assert "* Initial alpha rele" in log["0.0.5"]
    assert "* Added enforcement " in log["0.0.6"]


def test_aiobotocore_mirror():
    log = changelogs.get("aiobotocore_mirror")
    assert "* Initial alpha rele" in log["0.0.5"]


def test_aiocoap():
    log = changelogs.get("aiocoap")
    assert "Features" in log["0.3"]


def test_aiocouchdb():
    log = changelogs.get("aiocouchdb")
    assert "- Initial checkpoint" in log["0.1.0"]
    assert "- Second checkpoint " in log["0.2.0"]
    assert "- Third checkpoint r" in log["0.3.0"]
    assert "- Another checkpoint" in log["0.4.0"]
    assert "- Last checkpoint re" in log["0.5.0"]
    assert "- Adopt test suite t" in log["0.6.0"]
    assert "- Greatly improved m" in log["0.7.0"]


def test_aiocron():
    log = changelogs.get("aiocron")
    assert "Initial release" in log["0.1"]
    assert "Allow to use crontab" in log["0.2"]
    assert "- Fix installation f" in log["0.3"]
    assert "-  Fix contstructor " in log["0.4"]
    assert "- Fix: Initialize cr" in log["0.5"]
    assert "- allow to use pytho" in log["0.6"]
    assert "- Nothing changed ye" in log["0.7"]


def test_aiodjango():
    log = changelogs.get("aiodjango")
    assert "Initial packaged rel" in log["0.1"]
    assert "- Added support for " in log["0.2"]


def test_aiodns():
    log = changelogs.get("aiodns")
    assert "- Initial release" in log["0.1.0"]
    assert "- Add support for Tr" in log["0.2.0"]
    assert "- Add DNSResolver.ca" in log["0.3.0"]
    assert "- Adapt to Trollius " in log["0.3.1"]
    assert "- setup: Fix decodin" in log["0.3.2"]
    assert "- Use pycares >= 1.0" in log["1.0.0"]
    assert "- Fix including test" in log["1.0.1"]


def test_aioes():
    log = changelogs.get("aioes")
    assert "* Initial release" in log["0.1.0"]
    assert "* Make compatible wi" in log["0.2.0"]
    assert "* Use aiohttp.Client" in log["0.3.0"]
    assert "* Fix ES2+ compatibi" in log["0.4.0"]
    assert "* Allow scheme, user" in log["0.5.0"]
    assert "* Add support for ve" in log["0.6.0"]
    assert "* Accept bytes as pa" in log["0.6.1"]


def test_aioeventlet():
    log = changelogs.get("aioeventlet")
    assert "* First public relea" in log["0.1"]
    assert "aiogreen event loop " in log["0.2"]
    assert "* :func:`wrap_greent" in log["0.3"]
    assert "* Add run_aiotest.py" in log["0.4"]
    assert "* Unit tests now use" in log["0.5"]
    assert "* Fix EventLoop.stop" in log["0.5.1"]


def test_aioftp():
    log = changelogs.get("aioftp")
    assert "- first release (cli" in log["0.0.1"]
    assert "- server functionali" in log["0.1.0"]
    assert "- typos in server st" in log["0.1.1"]
    assert "- MemoryPathIO.Stats" in log["0.1.3"]
    assert "- close data connect" in log["0.1.4"]
    assert "- bugfix server on w" in log["0.1.5"]
    assert "- bugfix on windows " in log["0.1.6"]


def test_aiogibson():
    log = changelogs.get("aiogibson")
    assert "* Initial release;" in log["0.1.0"]
    assert "* Improved protocol " in log["0.1.1"]
    assert "* Changed Reader int" in log["0.1.2"]
    assert "* Documentation publ" in log["0.1.3"]


def test_aioh2():
    log = changelogs.get("aioh2")
    assert "* First release on P" in log["0.1.0"]


def test_aiohdfs():
    log = changelogs.get("aiohdfs")
    assert "*" in log["0.1.2"]
    assert "* Add Python 3 suppo" in log["0.3.0"]
    assert "* Fix print statemen" in log["0.3.2"]


def test_aiohttp():
    log = changelogs.get("aiohttp")
    assert "- Extract `BaseReque" in log["1.2.0"]


def test_alembic_verify():
    log = changelogs.get("alembic_verify")
    assert "Released 2016-10-19" in log["0.1.2"]
    assert "Released 2016-11-29" in log["0.1.3"]
    assert "Released 2016-11-30" in log["0.1.4"]


def test_alertlogic():
    log = changelogs.get("alertlogic")
    assert "* Ported from urllib" in log["0.2.0"]
    assert "* Added claim_applia" in log["0.3.0"]
    assert "* Updated to work wi" in log["0.4.0"]
    assert "* Fixed install bug " in log["0.4.1"]
    assert "* Fixed a bug in put" in log["0.4.2"]


def test_alfajor():
    log = changelogs.get("alfajor")
    assert "- Initial public alp" in log["0.1"]


def test_algebraixlib():
    log = changelogs.get("algebraixlib")
    assert "-   Initial release." in log["1.1"]
    assert "-   Major improvemen" in log["1.2"]
    assert "-   ``Atom``:" in log["1.3"]


def test_algoliasearch():
    log = changelogs.get("algoliasearch")
    assert "* Add `attribute_to_" in log["1.10.0"]
    assert "* Add `search_for_fa" in log["1.10.1"]
    assert "* Configure DNS reso" in log["1.11.0"]
    assert "* Add method to forw" in log["1.5.3"]
    assert "* Add new methods to" in log["1.5.4"]
    assert "* Fix issue with non" in log["1.5.5"]
    assert "* Add the ability to" in log["1.5.8"]


def test_algoliasearch_django():
    log = changelogs.get("algoliasearch_django")
    assert "* [REMOVE] algolia_b" in log["1.2.0"]
    assert "* [ADD] `get_queryse" in log["1.2.1"]
    assert "* [FIX] Compatibilit" in log["1.2.2"]
    assert "* [FIX] Check that g" in log["1.2.3"]


def test_algoliasearchasync():
    log = changelogs.get("algoliasearchasync")
    assert "* Add `searcH_for_fa" in log["1.0"]
    assert "* Remove DNS caching" in log["1.1"]


def test_alignment():
    log = changelogs.get("alignment")
    assert "- Better README file" in log["1.0.3"]
    assert "- Add PyPy support." in log["1.0.4"]
    assert "- Do not search alte" in log["1.0.7"]
    assert "- Make it compatible" in log["1.0.9"]


def test_alipay():
    log = changelogs.get("alipay")
    assert "- first commit" in log["0.1"]
    assert "- add unittest" in log["0.2"]
    assert "- fix rst doc" in log["0.2.1"]
    assert "- add includeme func" in log["0.2.2"]
    assert "- english version re" in log["0.2.3"]
    assert "- Add wap payment su" in log["0.3"]
    assert "- Seller id support" in log["0.4"]


def test_alkey():
    log = changelogs.get("alkey")
    assert "Initial version." in log["0.1"]
    assert "* only invalidate to" in log["0.2"]
    assert "* maintain table wri" in log["0.2.2"]
    assert "* bug fix model clas" in log["0.2.3"]
    assert "* fix major bug caus" in log["0.3"]
    assert "* add optional ``alk" in log["0.3.1"]
    assert "* provide a reified " in log["0.4"]


def test_allanon():
    log = changelogs.get("allanon")
    assert "- first release" in log["0.1"]
    assert "- Do not crawl or do" in log["0.2"]
    assert "- Performing a ``Key" in log["0.3"]


def test_allauth_watchdog_id():
    log = changelogs.get("allauth_watchdog_id")
    assert "* First release on P" in log["0.1.0"]


def test_allensdk():
    log = changelogs.get("allensdk")
    assert "Added" in log["0.10.0"]
    assert "Added" in log["0.10.1"]
    assert "Added" in log["0.11.0"]
    assert "Added" in log["0.12.0"]
    assert "Changed" in log["0.12.1"]
    assert "Fixed" in log["0.12.2"]
    assert "Fixed" in log["0.12.4"]


def test_allmychanges():
    log = changelogs.get("allmychanges")
    assert "* First version of i" in log["0.1.0"]
    assert "* Added new command " in log["0.2.0"]
    assert "* Commands' descript" in log["0.2.1"]
    assert "* Utility was fixed " in log["0.3.0"]
    assert "* Option `debug = tr" in log["0.4.0"]
    assert "* For case when chan" in log["0.5.0"]
    assert "* Fixed data import " in log["0.5.1"]


def test_allocine_wrapper():
    log = changelogs.get("allocine_wrapper")
    assert "* Original release" in log["0.1.0"]
    assert "* main class: Alloci" in log["0.2.0"]
    assert "* Use global dict fo" in log["0.3.0"]


def test_alm_solrindex():
    log = changelogs.get("alm_solrindex")
    assert "- First release" in log["0.1"]
    assert "- Filter out invalid" in log["0.10"]
    assert "- A commit after an " in log["0.11"]
    assert "- PEP8 cleanup" in log["0.12"]
    assert "- commit to cleanup " in log["0.13"]
    assert "- Updated SolrConnec" in log["0.14"]
    assert "- Added a GenericSet" in log["0.2"]


def test_almond():
    log = changelogs.get("almond")
    assert "* First release on P" in log["0.1.0"]


def test_alnair():
    log = changelogs.get("alnair")
    assert "- First release" in log["0.1"]
    assert "- A few bug fixes" in log["0.1.1"]
    assert "- Implement the comm" in log["0.1.2"]
    assert "- Change the APIs (A" in log["0.2"]
    assert "- Add command-line i" in log["0.3"]
    assert "- Implement the mult" in log["0.3.2"]


def test_aloe():
    log = changelogs.get("aloe")
    assert "Added" in log["0.0.22"]
    assert "Fixed" in log["0.0.23"]
    assert "Added" in log["0.0.24"]
    assert "Fixed" in log["0.0.25"]
    assert "Fixed" in log["0.0.26"]
    assert "Fixed" in log["0.0.27"]
    assert "Fixed" in log["0.0.28"]


def test_aloe_django():
    log = changelogs.get("aloe_django")
    assert "Initial PyPI release" in log["0.0.1"]
    assert "Fixed" in log["0.0.10"]
    assert "Fixed" in log["0.0.11"]
    assert "Added" in log["0.0.12"]
    assert "Added" in log["0.0.13"]
    assert "Added" in log["0.0.14"]
    assert "Added" in log["0.0.15"]


def test_alogator():
    log = changelogs.get("alogator")
    assert "- Removed daemon and" in log["0.1.0"]
    assert "- Add treshold for i" in log["0.2.0"]


def test_aloisius():
    log = changelogs.get("aloisius")
    assert "- First release" in log["0.1"]
    assert "- Add support for pa" in log["0.2"]
    assert "- Increase paralleli" in log["0.2.1"]
    assert "- Publish aloisius t" in log["0.3"]


def test_alot():
    log = changelogs.get("alot")
    assert "This minor release i" in log["0.11"]
    assert "* extensive API docs" in log["0.20"]
    assert "* avoid traceback in" in log["0.21"]
    assert "* revised config syn" in log["0.3"]
    assert "* use separate datab" in log["0.3.1"]
    assert "* fix bad GPG signat" in log["0.3.2"]
    assert "* interpret (semicol" in log["0.3.3"]


def test_alotofeffort():
    log = changelogs.get("alotofeffort")
    assert "* First release on P" in log["0.1"]
    assert "* It works on Python" in log["0.2"]
    assert "* Only files that ha" in log["0.3"]
    assert "* Upgraded boto to 2" in log["0.4.0"]


def test_altair():
    log = changelogs.get("altair")
    assert "- Initial release of" in log["1.0"]
    assert "Major additions" in log["1.2"]


def test_altapay():
    log = changelogs.get("altapay")
    assert "- Basic API connecti" in log["0.1.dev0"]
    assert "- Complex payments a" in log["0.1.dev1"]
    assert "- Added ``altapay.Tr" in log["0.1.dev2"]
    assert "- Added missing apos" in log["0.1.dev3"]
    assert "- Addded ``altapay.T" in log["1.0"]
    assert "- Added ``altapay.Tr" in log["1.0.dev4"]
    assert "- Added ``altapay.Tr" in log["1.0.dev6"]


def test_altered_states():
    log = changelogs.get("altered_states")
    assert "Initial release." in log["0.8.0"]
    assert "* Alias `Expando` as" in log["0.8.1"]
    assert "* Updated test suite" in log["0.8.2"]
    assert "* Added a new API en" in log["0.8.5"]
    assert "* Better handling of" in log["0.8.6"]


def test_altgraph():
    log = changelogs.get("altgraph")
    assert "This is a minor feat" in log["0.10"]
    assert "This is a bugfix rel" in log["0.10.1"]
    assert "- There where no cla" in log["0.10.2"]
    assert "- Stabilize the orde" in log["0.11"]
    assert "- Added ``ObjectGrap" in log["0.12"]
    assert "- Issue 4: Graph._bf" in log["0.13"]
    assert "This is a minor feat" in log["0.7.0"]


def test_alto():
    log = changelogs.get("alto")
    assert "Initial public relea" in log["0.1"]
    assert "Fixed a bug where th" in log["0.1.1"]
    assert "Added support for fu" in log["0.2"]
    assert "Added highlighting o" in log["0.2.1"]
    assert "Added view and modul" in log["0.2.2"]
    assert "Added the ability to" in log["0.2.3"]
    assert "Added the ability to" in log["0.3.0"]


def test_amadeus():
    log = changelogs.get("amadeus")
    assert "* First release on P" in log["0.1.0"]


def test_amfm_decompy():
    log = changelogs.get("amfm_decompy")
    assert "- Initial release." in log["1.0.0"]
    assert "- 'f0_min' bug in pY" in log["1.0.1"]
    assert "- several bugs relat" in log["1.0.3"]
    assert "- segmentation fault" in log["1.0.4"]
    assert "- issue with the int" in log["1.0.5"]


def test_ami_push():
    log = changelogs.get("ami_push")
    assert "* First version" in log["0.1.0"]


def test_amico():
    log = changelogs.get("amico")
    assert "* Initial release" in log["1.0.0"]
    assert "* Fix bug with setti" in log["1.0.1"]


def test_amifinder():
    log = changelogs.get("amifinder")
    assert "FEATURES:" in log["0.0.1"]
    assert "FEATURES:" in log["0.0.2"]
    assert "FEATURES:" in log["0.0.3"]


def test_amitu_hstore():
    log = changelogs.get("amitu_hstore")
    assert "- Fist release of 1." in log["1.2"]
    assert "- added Python3 supp" in log["1.2.1"]
    assert "- test runner improv" in log["1.2.2"]
    assert "- added experimental" in log["1.2.3"]
    assert "- ``HSTORE_GLOBAL_RE" in log["1.2.4"]
    assert "- introduced ``DJANG" in log["1.2.5"]
    assert "- schema mode" in log["1.3.0"]


def test_amitu_websocket_client():
    log = changelogs.get("amitu_websocket_client")
    assert "* Initial release." in log["0.1.0"]
    assert "* Added timeout" in log["0.1.1"]


def test_amitu_zutils():
    log = changelogs.get("amitu_zutils")
    assert "Initial release." in log["0.1.0"]


def test_amo2kinto():
    log = changelogs.get("amo2kinto")
    assert "- Create collection " in log["0.1.0"]
    assert "- kinto2xml was rena" in log["1.0.0"]
    assert "- In case there is a" in log["1.1.0"]
    assert "- Add functional tes" in log["1.2.0"]
    assert "- kinto_client.delet" in log["1.2.1"]
    assert "- Update records tha" in log["1.3.0"]
    assert "- Fix patch_records " in log["1.3.1"]


def test_amp():
    log = changelogs.get("amp")
    assert "* Added tests packag" in log["1.1"]
    assert "* Updated test cases" in log["1.1.1"]
    assert "* Fixed issue with t" in log["1.1.2"]
    assert "* Updated readme and" in log["1.1.3"]
    assert "* Updated URL" in log["1.1.4"]


def test_amphora():
    log = changelogs.get("amphora")
    assert "* Creating/deleting " in log["0.1.1"]
    assert "* Added ``AmqpRpcSer" in log["0.1.2"]
    assert "* Major changes in r" in log["0.1.3"]


def test_amplecode_recipe_template():
    log = changelogs.get("amplecode_recipe_template")
    assert "* Initial version" in log["0.1"]
    assert "* Stripping all opti" in log["0.1.1"]
    assert "* Added base-dir opt" in log["1.0"]
    assert "* Replaced iterable " in log["1.1"]
    assert "* All necessary subd" in log["1.2"]


def test_amqp():
    log = changelogs.get("amqp")
    assert "- Supports draining " in log["0.9.1"]
    assert "- Consumer cancel no" in log["0.9.2"]
    assert "- Fixed bug that cou" in log["0.9.3"]
    assert "- Adds support for `" in log["0.9.4"]
    assert ":release-date: 2012-" in log["1.0.0"]
    assert ":release-date: 2012-" in log["1.0.1"]
    assert ":release-date: 2013-" in log["1.0.10"]


def test_amqp_dispatcher():
    log = changelogs.get("amqp_dispatcher")
    assert "- V0.0.10. [Jose Dia" in log["0.0.10"]
    assert "- Use parameters whe" in log["0.0.3"]
    assert "- V0.0.4. [Philip Cr" in log["0.0.4"]
    assert "- V0.0.5. [Philip Cr" in log["0.0.5"]
    assert "- V0.0.6. [Philip Cr" in log["0.0.6"]
    assert "- Include version. [" in log["0.0.7"]
    assert "- V0.0.8 Fix bug whe" in log["0.0.8"]


def test_amqp_storm():
    log = changelogs.get("amqp_storm")
    assert "- Removed noisy logg" in log["1.3.0"]
    assert "- Fixed SSL bug that" in log["1.3.1"]
    assert "- Fixed minor bug in" in log["1.3.2"]
    assert "- Fixed bug causing " in log["1.3.3"]
    assert "- Dropped Python 3.2" in log["1.3.4"]
    assert "- 100% Unit-test Cov" in log["1.4.0"]
    assert "- Heartbeats are now" in log["1.4.1"]


def test_amqpeek():
    log = changelogs.get("amqpeek")
    assert "Released 2016-10-11" in log["0.0.1"]


def test_amqplib():
    log = changelogs.get("amqplib")
    assert "Initial version" in log["0.1"]
    assert "Changed the default " in log["0.2"]
    assert "Improved skeleton ge" in log["0.3"]
    assert "Get rid of Python 2." in log["0.5"]
    assert "Very large rearrange" in log["0.6"]
    assert "One minor change to " in log["0.6.1"]
    assert "Big speedup for send" in log["1.0.0"]


def test_amqpstorm():
    log = changelogs.get("amqpstorm")
    assert "- Removed noisy logg" in log["1.3.0"]
    assert "- Fixed SSL bug that" in log["1.3.1"]
    assert "- Fixed minor bug in" in log["1.3.2"]
    assert "- Fixed bug causing " in log["1.3.3"]
    assert "- Dropped Python 3.2" in log["1.3.4"]
    assert "- 100% Unit-test Cov" in log["1.4.0"]
    assert "- Heartbeats are now" in log["1.4.1"]


def test_amt():
    log = changelogs.get("amt")
    assert "* First release on P" in log["0.1.0"]
    assert "* python 3 print fix" in log["0.3.0"]
    assert "* python 3 fixes and" in log["0.4.0"]
    assert "* python 2 fixes for" in log["0.5.0"]
    assert "* add support for st" in log["0.6.0"]


def test_browsercookiejar():
    log = changelogs.get("browsercookiejar")
    assert "- Initial release" in log["0.1"]


def test_browsermob_proxy():
    log = changelogs.get("browsermob_proxy")
    assert "* Initial version" in log["0.0.1"]
    assert "* Removed httplib2 i" in log["0.1.0"]
    assert "* DELETE /proxy/:por" in log["0.2.0"]
    assert "* Allow setting basi" in log["0.4.0"]
    assert "* Allow proxying of " in log["0.5.0"]
    assert "* Added support for " in log["0.6.0"]
    assert "* Updating travis ci" in log["0.7.0"]


def test_browserstacker():
    log = changelogs.get("browserstacker")
    assert "* Added `make_screen" in log["0.2.1"]
    assert "* Changed commands n" in log["0.3.1"]
    assert "* Added verbose outp" in log["11.02.2016"]
    assert "* Initial release." in log["22.01.2016"]
    assert "* Used single `reque" in log["25.01.2016"]


def test_brubeck():
    log = changelogs.get("brubeck")
    assert "* [Feature] Official" in log["0.4.0"]


def test_bruges():
    log = changelogs.get("bruges")
    assert "Added AVO reflection" in log["0.1.1"]
    assert "Added data edge hand" in log["0.1.2"]
    assert "made time to depth c" in log["0.1.3"]
    assert "Added noise utility " in log["0.1.4"]
    assert "Added keywords and c" in log["0.1.5"]
    assert "Float conversion in " in log["0.1.6"]


def test_brush():
    log = changelogs.get("brush")
    assert "*2016-04-11*" in log["1.0"]
    assert "* Added a web interf" in log["1.0.0"]
    assert "*2016-06-29*" in log["1.1"]
    assert "*2016-07-18*" in log["1.2"]


def test_bsdconv():
    log = changelogs.get("bsdconv")
    assert "First tag, conversio" in log["0.120090419"]
    assert "Make hibernating wor" in log["0.220090507"]
    assert "Support callback in " in log["0.320090512"]
    assert "Bugfixes & Refactori" in log["0.420090514"]
    assert "Support alias" in log["0.520090518"]
    assert "Support various type" in log["0.620090520"]
    assert "Bugfixes & Cleanup" in log["0.720090523"]


def test_bsdiff4():
    log = changelogs.get("bsdiff4")
    assert "initial release" in log["1.0.0"]
    assert "* add example which " in log["1.0.1"]
    assert "* add Python 3 suppo" in log["1.1.0"]
    assert "* while performing t" in log["1.1.1"]
    assert "* fixed file_patch w" in log["1.1.2"]
    assert "* fixed file_patch()" in log["1.1.3"]
    assert "* fix Python 3 issue" in log["1.1.4"]


def test_bsdploy():
    log = changelogs.get("bsdploy")
    assert "- added bsdploy.fabu" in log["1.0.0"]
    assert "- Initial public rel" in log["1.0b1"]
    assert "- migrate from ``mr." in log["1.0b2"]
    assert "- make ``ploy_virtua" in log["1.0b3"]
    assert "- remove custom ``pl" in log["1.0b4"]
    assert "- use FreeBSD 10.0 a" in log["1.1.0"]
    assert "- increase memory fo" in log["1.1.1"]


def test_bson_lazy():
    log = changelogs.get("bson_lazy")
    assert "* Initial release." in log["0.1"]
    assert "* Introduced a simpl" in log["0.2"]
    assert "* bson2json.py: Catc" in log["0.2.1"]
    assert "* bson.load(): Inval" in log["0.2.2"]
    assert "* Fixed version hist" in log["0.2.4"]


def test_bst_pygasus_core():
    log = changelogs.get("bst_pygasus_core")
    assert "- Initial public rel" in log["1.0"]
    assert "- Use complete MANIF" in log["1.0.1"]
    assert "- Nothing changed ye" in log["1.1"]


def test_bst_pygasus_datamanager():
    log = changelogs.get("bst_pygasus_datamanager")
    assert "- Initial public rel" in log["1.0"]
    assert "- Use complete MANIF" in log["1.0.1"]
    assert "- Nothing changed ye" in log["1.1"]


def test_bst_pygasus_demo():
    log = changelogs.get("bst_pygasus_demo")
    assert "- Initial public rel" in log["1.0"]
    assert "- adding pgp signatu" in log["1.0.1"]
    assert "- Use complete MANIF" in log["1.0.2"]
    assert "- Nothing changed ye" in log["1.1"]


def test_bst_pygasus_i18n():
    log = changelogs.get("bst_pygasus_i18n")
    assert "- Initial public rel" in log["1.0"]
    assert "- Use complete MANIF" in log["1.0.1"]
    assert "- Nothing changed ye" in log["1.1"]


def test_bst_pygasus_resources():
    log = changelogs.get("bst_pygasus_resources")
    assert "- Initial public rel" in log["1.0"]
    assert "- Use complete MANIF" in log["1.0.1"]
    assert "- Nothing changed ye" in log["1.1"]


def test_bst_pygasus_security():
    log = changelogs.get("bst_pygasus_security")
    assert "- Initial public rel" in log["1.0"]
    assert "- Use complete MANIF" in log["1.0.1"]
    assert "- Nothing changed ye" in log["1.1"]


def test_bst_pygasus_session():
    log = changelogs.get("bst_pygasus_session")
    assert "- Initial public rel" in log["1.0"]
    assert "- Use complete MANIF" in log["1.0.1"]
    assert "- Nothing changed ye" in log["1.1"]


def test_bst_pygasus_wsgi():
    log = changelogs.get("bst_pygasus_wsgi")
    assert "- Initial public rel" in log["1.0"]
    assert "- Use complete MANIF" in log["1.0.1"]
    assert "- Nothing changed ye" in log["1.1"]


def test_btcndash():
    log = changelogs.get("btcndash")
    assert "* Initial release." in log["0.1.0"]
    assert "* Added a more grace" in log["0.1.1"]
    assert "* Bumped version to " in log["1.0.0"]
    assert "* Fixed a bug with f" in log["1.0.1"]
    assert "* Significant refact" in log["2.0.0"]
    assert "* Return config file" in log["2.1.0"]
    assert "* Added interactive " in log["2.2.0"]


def test_btnamespace():
    log = changelogs.get("btnamespace")
    assert "released 2014-04-07" in log["1.0.0"]
    assert "released 2014-04-08" in log["1.0.1"]
    assert "released 2014-07-28" in log["1.1.0"]
    assert "released 2014-09-26" in log["1.1.1"]
    assert "released 2016-07-15" in log["2.0.0"]


def test_btparser():
    log = changelogs.get("btparser")
    assert "* First release on P" in log["0.1.0"]


def test_bts_proxy():
    log = changelogs.get("bts_proxy")
    assert "* first public relea" in log["0.1"]


def test_bts_tools():
    log = changelogs.get("bts_tools")
    assert "* first public relea" in log["0.1"]
    assert "* added view for con" in log["0.1.1"]
    assert "* modularized monito" in log["0.1.10"]
    assert "* updated for buildi" in log["0.1.2"]
    assert "* renamed project fr" in log["0.1.3"]
    assert "* now publishes feed" in log["0.1.4"]
    assert "* smarter caching of" in log["0.1.5"]


def test_btx():
    log = changelogs.get("btx")
    assert "- Initial release" in log["0.0.1"]


def test_bubbles():
    log = changelogs.get("bubbles")
    assert "Overview" in log["0.2"]


def test_buccaneer():
    log = changelogs.get("buccaneer")
    assert "* forked from pelica" in log["3.6.0"]
    assert "* bugfix for develop" in log["3.6.25"]
    assert "* target_blank plugi" in log["3.6.26"]
    assert "* plugin optimize_im" in log["3.6.32"]
    assert "* ported gzip_cache " in log["3.7.0"]
    assert "* AWS s3 fix for buc" in log["3.7.1"]
    assert "* sync feature (remo" in log["3.7.10"]


def test_bucky():
    log = changelogs.get("bucky")
    assert "* [FIX] Change githu" in log["0.3.0"]
    assert "* [FIX] setup.py" in log["0.3.1"]
    assert "* [NEW] Allow Bucky " in log["2.0.0"]
    assert "* [NEW] Processor ho" in log["2.2.0"]
    assert "* [NEW] Python Packa" in log["2.2.1"]
    assert "* [FIX] Persisting g" in log["2.2.2"]
    assert "* [NEW] Sets" in log["2.3.0"]


def test_bufferkdtree():
    log = changelogs.get("bufferkdtree")
    assert "* First major releas" in log["1.0"]
    assert "* Adapted building p" in log["1.0.1"]
    assert "* Adapted building p" in log["1.0.2"]
    assert "* Fixed wrong parame" in log["1.1"]
    assert "* Updated documentat" in log["1.1.1"]
    assert "* Added support for " in log["1.2"]
    assert "* Updated documentat" in log["1.3"]


def test_bugsy():
    log = changelogs.get("bugsy")
    assert "* Initial implementa" in log["0.1.0"]
    assert "* Added the ability " in log["0.2.0"]
    assert "* Updated Documentat" in log["0.3.0"]
    assert "* Add in the ability" in log["0.4.0"]
    assert "* remove unused impo" in log["0.4.1"]
    assert "* Add the ability to" in log["0.5.0"]
    assert "* Update flake8 conf" in log["0.6.0"]


def test_bugwarrior():
    log = changelogs.get("bugwarrior")
    assert "- Support for megapl" in log["0.5.4"]
    assert "- Support for TeamLa" in log["0.5.5"]
    assert "- support for jira t" in log["0.5.6"]
    assert "- Added list of cont" in log["0.5.7"]
    assert "- Typofix in docs. `" in log["0.5.8"]
    assert "- First run at multi" in log["0.6.0"]
    assert "- Make the jira serv" in log["0.6.1"]


def test_bugzilla2fedmsg():
    log = changelogs.get("bugzilla2fedmsg")
    assert "- Include .rst files" in log["0.1.2"]
    assert "- License LGPLv2+. `" in log["0.1.3"]
    assert "- Ignore certs and s" in log["0.2.0"]
    assert "- Handle timezones. " in log["0.2.1"]
    assert "Pull Requests" in log["0.3.0"]


def test_bugzillatools():
    log = changelogs.get("bugzillatools")
    assert "New features:" in log["0.1"]
    assert "New features:" in log["0.1.1"]
    assert "Bug fixes:" in log["0.1.2"]
    assert "New features:" in log["0.2"]
    assert "Bug fixes:" in log["0.2.1"]
    assert "New features:" in log["0.3"]
    assert "New features:" in log["0.4"]


def test_build_commands():
    log = changelogs.get("build_commands")
    assert "-  Initial version" in log["0.0.1"]
    assert "- Nothing changed ye" in log["0.0.2"]


def test_buildbot_travis():
    log = changelogs.get("buildbot_travis")
    assert "- Initial release" in log["0.0.0"]
    assert "- Builds triggered b" in log["0.0.1"]
    assert "- Nothing changed ye" in log["0.0.10"]
    assert "- Fix manifest to in" in log["0.0.11"]
    assert "- Nothing changed ye" in log["0.0.12"]
    assert "- Only show pending " in log["0.0.13"]
    assert "- UI hints during gr" in log["0.0.14"]


def test_buildchecker():
    log = changelogs.get("buildchecker")
    assert "* First release on P" in log["0.1.0"]


def test_buildfox():
    log = changelogs.get("buildfox")
    assert "- Initial version" in log["0.1"]
    assert "- Fixed library tran" in log["0.2"]


def test_buildout_helpers():
    log = changelogs.get("buildout_helpers")
    assert "- Initial release." in log["0.1"]
    assert "- Support piping." in log["0.2.0"]
    assert "- Mr.developer varia" in log["0.3.0"]
    assert "- This package is wo" in log["1.0.0"]
    assert "- Add freeze command" in log["1.0.0b1"]
    assert "- Mostly refactor fr" in log["1.0.0b2"]
    assert "- Now normalize_buil" in log["1.0.0b3"]


def test_buildout_script():
    log = changelogs.get("buildout_script")
    assert "* Initial public rel" in log["0.1"]
    assert "* Implemented ``temp" in log["0.2a1"]
    assert "* Fixes to make reci" in log["0.2a2"]
    assert "* Templating syntax " in log["0.2a3"]
    assert "* PyPI release of ch" in log["0.3"]


def test_buildout_autoextras():
    log = changelogs.get("buildout_autoextras")
    assert "- Initial release. [" in log["1.0"]
    assert "- Monkeypatching zc." in log["1.1"]
    assert "- no changes" in log["1.2"]


def test_buildout_disablessl():
    log = changelogs.get("buildout_disablessl")
    assert "initial release" in log["1.0"]
    assert "- Disable SSL certif" in log["1.1"]
    assert "- Nothing changed ye" in log["1.2"]


def test_buildout_dumppickedversions2():
    log = changelogs.get("buildout_dumppickedversions2")
    assert "- Initial version" in log["1.0"]
    assert "- Fixed an issue wit" in log["1.0.1"]
    assert "- Explicitly require" in log["1.0.2"]
    assert "- Uses the new picke" in log["1.1"]
    assert "- Nothing changed ye" in log["1.1.1"]


def test_buildout_eggscleaner():
    log = changelogs.get("buildout_eggscleaner")
    assert "- Creation" in log["0.1"]
    assert "- Redid documentatio" in log["0.1.5"]
    assert "- Make eggscleaner r" in log["0.1.6"]
    assert "- Bump version to fi" in log["0.1.7"]


def test_buildout_gc():
    log = changelogs.get("buildout_gc")
    assert "- Creation" in log["0.1"]
    assert "- Redid documentatio" in log["0.1.5"]
    assert "- Created public for" in log["1.0"]
    assert "- Fixed incorrect me" in log["1.2.dev"]


def test_buildout_minitagificator():
    log = changelogs.get("buildout_minitagificator")
    assert "* Initial release" in log["1.0"]
    assert "* packaging" in log["1.1"]
    assert "* code cometics" in log["1.4"]
    assert "* Refactor code" in log["1.5"]
    assert "* Get an absolute pa" in log["1.6"]
    assert "- 1.0 compatibility" in log["2.0"]
    assert "* fix tests (the onl" in log["2.1"]


def test_buildout_packagename():
    log = changelogs.get("buildout_packagename")
    assert "- Initial release." in log["1.0"]


def test_django_strategy_field():
    log = changelogs.get("django_strategy_field")
    assert "* initial release" in log["0.1"]
    assert "* Django 1.9 support" in log["0.2"]
    assert "* Django 1.10 suppor" in log["0.3"]
    assert "* fixes bug wit DRF" in log["0.4"]
    assert "* fixes bugs for emp" in log["0.5"]
    assert "* add 'display_attri" in log["1.0"]


def test_django_su():
    log = changelogs.get("django_su")
    assert "c55b117d4d	Updating " in log["0.3.0"]
    assert "81e27c1c0f	Adding lo" in log["0.3.1"]
    assert "3021ad7e73	Minor rea" in log["0.3.2"]
    assert "65a365df3c	Remove de" in log["0.4.0"]
    assert "177d5cb7ed	Fixed imp" in log["0.4.1"]
    assert "c9ffb78d8a	Fixed 23 " in log["0.4.2"]
    assert "30fe67b924	Fix login" in log["0.4.3"]


def test_django_sub_query():
    log = changelogs.get("django_sub_query")
    assert "* First release on P" in log["0.1.0"]


def test_django_subcommand():
    log = changelogs.get("django_subcommand")
    assert "* Alpha" in log["0.0.1"]
    assert "* Remove the django_" in log["0.0.2"]
    assert "* Fixed issue 1 - un" in log["0.3.2"]


def test_django_subcommand2():
    log = changelogs.get("django_subcommand2")
    assert "* First release on P" in log["0.1.0"]
    assert "* Update badges." in log["0.1.1"]


def test_django_subdomain_instances():
    log = changelogs.get("django_subdomain_instances")
    assert "Initial release." in log["0.1"]
    assert "Add translation of f" in log["0.10"]
    assert "Include better waiti" in log["0.10.1"]
    assert "Add Spanish translat" in log["0.10.2"]
    assert "Include migration re" in log["0.10.3"]
    assert "Bugfix for when BASE" in log["0.2"]
    assert "Easy test running an" in log["0.3"]


def test_django_subs():
    log = changelogs.get("django_subs")
    assert "* Initial commit." in log["0.1.0"]


def test_django_subscribe():
    log = changelogs.get("django_subscribe")
    assert "Initial commit" in log["0.1"]
    assert "- Fixed wrong templa" in log["0.1.1"]
    assert "- Fixed some wrong p" in log["0.1.2"]
    assert "- Added related_name" in log["0.1.3"]
    assert "- redirecting to the" in log["0.1.4"]
    assert "- Added new migratio" in log["0.1.5"]


def test_django_suit():
    log = changelogs.get("django_suit")
    assert "* First stable versi" in log["0.1.0"]
    assert "* [Feature] Added li" in log["0.1.1"]
    assert "* [Feature] Customiz" in log["0.1.2"]
    assert "* [Feature] `Sortabl" in log["0.1.3"]
    assert "* [Fix] Sortables im" in log["0.1.4"]
    assert "* [Feature] New widg" in log["0.1.5"]
    assert "* [Tests] Travis CI " in log["0.1.6"]


def test_django_suit_dashboard():
    log = changelogs.get("django_suit_dashboard")
    assert "* Alpha release on P" in log["0.1.0"]


def test_django_suit_locale():
    log = changelogs.get("django_suit_locale")
    assert "* Initial version wi" in log["1.0.0"]
    assert "* Added Czech transl" in log["1.0.1"]
    assert "* Add Spanish (Argen" in log["1.0.10"]
    assert "* Added French trans" in log["1.0.2"]
    assert "* Added Turkish tran" in log["1.0.3"]
    assert "* Added Polish trans" in log["1.0.4"]
    assert "* Added Russian tran" in log["1.0.5"]


def test_django_suit_rq():
    log = changelogs.get("django_suit_rq")
    assert "Initial version." in log["1.0.0"]


def test_django_suit_sortable():
    log = changelogs.get("django_suit_sortable")
    assert "* First release on G" in log["0.1.0"]


def test_django_summernote():
    log = changelogs.get("django_summernote")
    assert "0.1.0 - Initial rele" in log["0.2.0"]


def test_django_sunset():
    log = changelogs.get("django_sunset")
    assert "*Release date: 05-No" in log["0.1"]
    assert "*Release date: 24-No" in log["0.2"]
    assert "*Release data: 31-Ma" in log["0.3"]


def test_django_superform():
    log = changelogs.get("django_superform")
    assert "* Initial release wi" in log["0.1.0"]
    assert "* Django 1.8 support" in log["0.2.0"]
    assert "* `11`_: Fix ``Compo" in log["0.3.0"]
    assert "* ``SuperForm.compos" in log["0.3.1"]


def test_django_supervisor():
    log = changelogs.get("django_supervisor")
    assert "* Initial release; y" in log["0.1.0"]
    assert "and restarts all pro" in log["0.1.1"]
    assert "* More flexibility i" in log["0.2.0"]
    assert "* Stop manage.py try" in log["0.2.1"]
    assert "* Explicitly use {{ " in log["0.2.2"]
    assert "`manage.py superviso" in log["0.2.3"]
    assert "* Support for Django" in log["0.2.4"]


def test_django_support_tickets():
    log = changelogs.get("django_support_tickets")
    assert "* First release on P" in log["0.1.0"]



def test_gwrappy():
    log = changelogs.get("gwrappy")
    assert "* New and improved v" in log["0.1.0"]
    assert "* Completed docstrin" in log["0.1.1"]
    assert "* Bug Fixes" in log["0.1.2"]
    assert "* BigQuery:" in log["0.1.3"]
    assert "* gwrappy.errors no " in log["0.1.4"]
    assert "* list methods now r" in log["0.1.5"]
    assert "* Added more utiliti" in log["0.1.6"]


def test_gxformat2():
    log = changelogs.get("gxformat2")
    assert "* Initial version - " in log["0.1.0"]
    assert "* Fix one Python 3 i" in log["0.1.1"]


def test_gyroid():
    log = changelogs.get("gyroid")
    assert "* Released at 2012.3" in log["0.1"]
    assert "* Made several optim" in log["0.2"]
    assert "* Basis.generate_str" in log["0.3"]
    assert "* Add more symmetry " in log["0.4"]


def test_gzbus():
    log = changelogs.get("gzbus")
    assert "- Initial version." in log["0.1.0"]
    assert "- Fix installation i" in log["0.1.1"]


def test_gzip_reader():
    log = changelogs.get("gzip_reader")
    assert "- initial version" in log["0.1"]


def test_h2o_pysparkling_1_6():
    log = changelogs.get("h2o_pysparkling_1_6")
    assert "- Upgraded H2O dev t" in log["0.2.12"]
    assert "- Upgrade h2o depend" in log["0.2.13"]
    assert "- Upgrade h2o depend" in log["0.2.14"]
    assert "- Major release of S" in log["1.2.0"]
    assert "- Major release of S" in log["1.3.0"]
    assert "- Support of primiti" in log["1.4.0"]
    assert "- Bug fixes" in log["1.6.1"]


def test_h2o_pysparkling_2_0():
    log = changelogs.get("h2o_pysparkling_2_0")
    assert "- Upgraded H2O dev t" in log["0.2.12"]
    assert "- Upgrade h2o depend" in log["0.2.13"]
    assert "- Upgrade h2o depend" in log["0.2.14"]
    assert "- Major release of S" in log["1.2.0"]
    assert "- Major release of S" in log["1.3.0"]
    assert "- Support of primiti" in log["1.4.0"]
    assert "- Bug fixes" in log["1.6.1"]


def test_h5cube():
    log = changelogs.get("h5cube")
    assert "Initial beta release" in log["0.1"]
    assert "Administrative fix (" in log["0.1.post1"]
    assert "* Improve wording of" in log["0.1.post2"]
    assert "Performance:" in log["0.2"]


def test_haas():
    log = changelogs.get("haas")
    assert "The initial release " in log["0.1.0"]
    assert "Enhancements" in log["0.2.0"]
    assert "Enhancements" in log["0.2.1"]
    assert "Enhancements" in log["0.2.2"]
    assert "Enhancements" in log["0.2.3"]
    assert "Bugs Fixed" in log["0.3.0"]
    assert "Bugs Fixed" in log["0.3.1"]


def test_habanero():
    log = changelogs.get("habanero")
    assert "* First pypi release" in log["0.0.6"]
    assert "* Now compatible wit" in log["0.1.0"]
    assert "* Fix readme" in log["0.1.1"]
    assert "* Fix wheel file to " in log["0.1.3"]
    assert "* user-agent strings" in log["0.2.0"]
    assert "* fixed some example" in log["0.2.2"]
    assert "* fixed problem with" in log["0.2.6"]


def test_habitat():
    log = changelogs.get("habitat")
    assert "- Initial release" in log["0.1"]
    assert "- Tests refactored a" in log["0.2"]


def test_hachi():
    log = changelogs.get("hachi")
    assert "* First release" in log["0.1"]
    assert "* Python 3 fixes" in log["0.2"]
    assert "* Python 2.7.3 fixes" in log["0.3"]
    assert "* Remove frame id at" in log["0.4"]
    assert "* Add supply_voltage" in log["0.5"]
    assert "* Add a close method" in log["0.5.1"]


def test_hack():
    log = changelogs.get("hack")
    assert "This was a large rel" in log["2.2.0"]
    assert "This was a large rel" in log["3.0.0"]
    assert "A small bugfix relea" in log["3.0.1"]
    assert "- Cherry-pick 695, a" in log["3.0.2"]
    assert "- Fixed some perform" in log["3.0.3"]
    assert "- Fixed a bug that m" in log["3.0.4"]
    assert "A number of smaller " in log["3.1.0"]


def test_hacker():
    log = changelogs.get("hacker")
    assert "* Conception" in log["0.0.1"]
    assert "* Initial Version!" in log["0.1.0"]
    assert "* Better documentati" in log["0.1.1"]
    assert "* py3k support" in log["0.2.0"]
    assert "* bug fix: reprs" in log["0.2.1"]
    assert "* bug fix: User's cr" in log["0.2.2"]


def test_hackernews():
    log = changelogs.get("hackernews")
    assert "- Fix: Publish time " in log["1.5.9"]
    assert "- Add: Tests" in log["1.6.0"]
    assert "- Add: Travis CI int" in log["1.6.1"]
    assert "- Add: Pagination" in log["1.6.2"]
    assert "- Fix: Python 3 comp" in log["1.6.3"]
    assert "- Add: Use `Story` c" in log["1.7.0"]
    assert "- Fix: `UnboundLocal" in log["1.7.1"]


def test_hackernews_python():
    log = changelogs.get("hackernews_python")
    assert "- 1st release" in log["0.1.0"]
    assert "- Improve syntax hig" in log["0.1.1"]
    assert "- Convert timestamps" in log["0.2.0"]
    assert "- Returns Item and U" in log["0.3.0"]
    assert "- Fix README example" in log["0.3.1"]


def test_hackertray():
    log = changelogs.get("hackertray")
    assert "* Sep 27, 2014" in log["2.3.2"]
    assert "* Oct 3, 2014" in log["3.0.0"]


def test_kinto_fxa():
    log = changelogs.get("kinto_fxa")
    assert "- Imported code from" in log["1.0.0"]
    assert "- Do not prefix auth" in log["1.1.0"]
    assert "It is now possible t" in log["1.2.0"]
    assert "- Multiple scopes ca" in log["1.3.0"]
    assert "- Separate multiple " in log["1.3.1"]
    assert "- In case the Oauth " in log["1.3.2"]
    assert "-  Updated to *Cliqu" in log["1.4.0"]


def test_kinto_http():
    log = changelogs.get("kinto_http")
    assert "- A client to synchr" in log["0.1.1"]
    assert "- Rename kintoclient" in log["0.2.0"]
    assert "- Rewrote the API to" in log["1.0.0"]
    assert "- Added support for " in log["2.0.0"]
    assert "- Updated the ``upda" in log["3.0.0"]
    assert "- Add CLI helpers to" in log["3.1.0"]
    assert "- The function ``cli" in log["4.0.0"]


def test_kinto_ldap():
    log = changelogs.get("kinto_ldap")
    assert "- Basic Auth Authent" in log["0.1.0"]
    assert "- Set default value " in log["0.2.0"]
    assert "- Fix heartbeat that" in log["0.2.1"]
    assert "- Support login from" in log["0.3.0"]
    assert "- Nothing changed ye" in log["0.4.0"]


def test_kinto_pusher():
    log = changelogs.get("kinto_pusher")
    assert "- Initial working pr" in log["0.1.0"]
    assert "- Add HTML demo with" in log["0.2.0"]
    assert "- Project renamed to" in log["0.3.0"]
    assert "- Add the plugin ver" in log["0.4.0"]
    assert "- Nothing changed ye" in log["0.5.0"]


def test_kinto_redis():
    log = changelogs.get("kinto_redis")
    assert "- Move the kinto red" in log["1.0.0"]
    assert "- Fix compability wi" in log["1.0.1"]
    assert "- Nothing changed ye" in log["1.1.0"]


def test_kinto_wizard():
    log = changelogs.get("kinto_wizard")
    assert "- Supports dumping/l" in log["1.0.0"]
    assert "- Nothing changed ye" in log["1.1.0"]


def test_kinto2xml():
    log = changelogs.get("kinto2xml")
    assert "- Create collection " in log["0.1.0"]
    assert "- kinto2xml was rena" in log["1.0.0"]
    assert "- In case there is a" in log["1.1.0"]
    assert "- Add functional tes" in log["1.2.0"]
    assert "- kinto_client.delet" in log["1.2.1"]
    assert "- Update records tha" in log["1.3.0"]
    assert "- Fix patch_records " in log["1.3.1"]


def test_kipart():
    log = changelogs.get("kipart")
    assert "____________________" in log["0.1.0"]
    assert "____________________" in log["0.1.1"]
    assert "____________________" in log["0.1.10"]
    assert "____________________" in log["0.1.11"]
    assert "____________________" in log["0.1.12"]
    assert "____________________" in log["0.1.13"]
    assert "____________________" in log["0.1.14"]


def test_kissanime_dl():
    log = changelogs.get("kissanime_dl")
    assert "Added quality argume" in log["1.2.0"]
    assert "Added txtlink argume" in log["1.3.0"]
    assert "Made cross platform " in log["1.4.0"]
    assert "Added Resuming Downl" in log["1.6"]
    assert "Added support for Ki" in log["1.8.0"]


def test_kit():
    log = changelogs.get("kit")
    assert "* Initial release" in log["0.1"]
    assert "* Allow several Flas" in log["0.2"]


def test_kitchen():
    log = changelogs.get("kitchen")
    assert "* Initial releae of " in log["0.1a1"]
    assert "* Fixes for python-2" in log["0.1a2"]
    assert "* Add a defaultdict " in log["0.1a3"]
    assert "* Fix failing unitte" in log["0.2.1a1"]
    assert "* Add kitchen.text.c" in log["0.2.2"]
    assert "* Fix exception mess" in log["0.2.2a1"]
    assert "* Expose MAXFD, list" in log["0.2.3"]


def test_kittyfuzzer():
    log = changelogs.get("kittyfuzzer")
    assert "* bugfix: [DataModel" in log["0.6.10"]
    assert "* bugfix: [Data Mana" in log["0.6.2"]
    assert "* bugfix: [Web Inter" in log["0.6.3"]
    assert "* bugfix: [package] " in log["0.6.4"]
    assert "* bugfix: [ClientFuz" in log["0.6.5"]
    assert "* bugfix: [WebInterf" in log["0.6.6"]
    assert "* bugfix: [BaseFuzze" in log["0.6.7"]


def test_kivy_okapi():
    log = changelogs.get("kivy_okapi")
    assert "- Initial Release" in log["0.1.0"]
    assert "- Rename `Game._move" in log["0.1.1"]


def test_klaus():
    log = changelogs.get("klaus")
    assert "* Rewrite/port to Fl" in log["0.2"]
    assert "* Tags work again (J" in log["0.2.1"]
    assert "* 49: Support for sh" in log["0.2.2"]
    assert "* Fix an issue with " in log["0.2.3"]
    assert "* 59: Show download " in log["0.3"]
    assert "* Moved ``klaus.wsgi" in log["0.4"]
    assert "* Bug 82: Include ``" in log["0.4.1"]


def test_klein():
    log = changelogs.get("klein")
    assert "* Initial release" in log["0.1.0"]
    assert "* Include headers wh" in log["0.1.1"]
    assert "* [BUG] Remove suppo" in log["0.2.0"]
    assert "* [BUG] Klein has be" in log["0.2.1"]
    assert "* [ENHANCEMENT] Klei" in log["0.2.2"]
    assert "* [BUG] Klein now co" in log["0.2.3"]
    assert "* [BUG] Klein now at" in log["14.0.0"]


def test_kliko():
    log = changelogs.get("kliko")
    assert "* Increased schema v" in log["0.3"]
    assert "* Added a command li" in log["0.6"]
    assert "* Install docker by " in log["0.7"]
    assert "* Run /kliko, not th" in log["0.7.1"]


def test_kloudi():
    log = changelogs.get("kloudi")
    assert "* feature: initial p" in log["0.1"]
    assert "* feature: initial p" in log["0.2"]
    assert "* feature: Add suppo" in log["0.3"]


def test_mrwolfe():
    log = changelogs.get("mrwolfe")
    assert "Initial release" in log["1.0.0a"]
    assert "* Fixed SLA view" in log["1.0.1a"]
    assert "* More reading mater" in log["1.0.2a"]
    assert "* Enabled skin plugi" in log["1.0.3a"]
    assert "* Added 'on hold' st" in log["1.0.4a"]
    assert "* Fixed broken searc" in log["1.0.5a"]
    assert "* Style consistency " in log["1.0.6a"]


def test_msaf():
    log = changelogs.get("msaf")
    assert "* Initial release" in log["0.0.1"]
    assert "* New features: Temp" in log["0.1.0"]
    assert "* Fixed plotting iss" in log["0.1.1"]
    assert "* Adapting code to l" in log["0.1.2"]
    assert "* Fixed bug of selec" in log["0.1.3"]
    assert "* Included Python 3." in log["0.1.4"]


def test_mschematool():
    log = changelogs.get("mschematool")
    assert "Initial release with" in log["0.5"]
    assert "* Apache Cassandra 2" in log["0.6"]
    assert "* Fixed ordering mig" in log["0.6.1"]
    assert "* init\_db command i" in log["0.6.2"]
    assert "* Fixed setup.py scr" in log["0.6.3"]
    assert "* setup.py from 0.6." in log["0.6.4"]
    assert "* Removed Python 3.4" in log["0.6.5"]


def test_msd():
    log = changelogs.get("msd")
    assert "* setup.py includes " in log["0.1.1"]
    assert "* fix severe bug in " in log["0.1.2"]
    assert "* eliminated single-" in log["0.1.3"]
    assert "* reads in YAML form" in log["0.1.4"]
    assert "* leave it to PyYAML" in log["0.1.5"]


def test_msgpack_numpy():
    log = changelogs.get("msgpack_numpy")
    assert "* First public relea" in log["0.01"]
    assert "* Add support for ms" in log["0.02"]
    assert "* Improve encoding/d" in log["0.021"]
    assert "* Fix decoding of st" in log["0.022"]
    assert "* Add support for ms" in log["0.03"]
    assert "* Switch to PEP 440 " in log["0.3.1"]
    assert "* Make package a sim" in log["0.3.1.1"]


def test_msgpack_python():
    log = changelogs.get("msgpack_python")
    assert ":release date: 2011-" in log["0.1.10"]
    assert ":release date: 2011-" in log["0.1.11"]
    assert ":release date: 2011-" in log["0.1.12"]
    assert ":release date: 2012-" in log["0.1.13"]
    assert ":release date: 2010-" in log["0.1.7"]
    assert ":release date: 2011-" in log["0.1.8"]
    assert ":release date: 2011-" in log["0.1.9"]


def test_msisdn_cli():
    log = changelogs.get("msisdn_cli")
    assert "- Detect verificatio" in log["1.0"]
    assert "- Nothing changed ye" in log["1.1"]


def test_mss():
    log = changelogs.get("mss")
    assert "- first release" in log["0.0.1"]
    assert "- new contributors: " in log["0.0.2"]
    assert "- MSS: remove PNG fi" in log["0.0.3"]
    assert "- Linux: use of memo" in log["0.0.4"]
    assert "- MSS: code simplifi" in log["0.0.5"]
    assert "- new contributor: S" in log["0.0.6"]
    assert "- MSS: fix path wher" in log["0.0.7"]


def test_mssqlcli():
    log = changelogs.get("mssqlcli")
    assert "New" in log["1.0.2"]


def test_mstranslator():
    log = changelogs.get("mstranslator")
    assert "- Added get_lang_nam" in log["0.2.1"]
    assert "- Added break_senten" in log["0.2.2"]
    assert "- Added get_translat" in log["0.2.3"]
    assert "- Added translate_ar" in log["0.2.4"]
    assert "- Fixed README forma" in log["0.2.5"]
    assert "- Translator API err" in log["0.2.6"]


def test_mtb():
    log = changelogs.get("mtb")
    assert "* [mp] first release" in log["0.1.0"]


def test_mtj_f3u1():
    log = changelogs.get("mtj_f3u1")
    assert "* Core functionality" in log["0.1"]
    assert "* Python 3 compatibi" in log["0.2"]


def test_mtj_jibber():
    log = changelogs.get("mtj_jibber")
    assert "- Core functions imp" in log["0.1"]
    assert "- Private chat messa" in log["0.2"]
    assert "- ``MucChatBot.send_" in log["0.3"]
    assert "- Fully require the " in log["0.4"]
    assert "- Provide Affilate C" in log["0.5"]


def test_mtools():
    log = changelogs.get("mtools")
    assert "This is the first ve" in log["1.0.0"]
    assert "* fixed timezone bug" in log["1.0.1"]
    assert "* mlogvis: doesn't r" in log["1.0.2"]
    assert "* mplotqueries: alwa" in log["1.0.3"]
    assert "* mlogvis: fixed a b" in log["1.0.4"]
    assert "* mplotqueries: incl" in log["1.0.5"]
    assert "Simpler Structure" in log["1.1.0"]


def test_mts():
    log = changelogs.get("mts")
    assert "* First release on P" in log["0.1.2"]
    assert "* Added uptobox hand" in log["0.3"]


def test_mucloud():
    log = changelogs.get("mucloud")
    assert "* Initial public rel" in log["1.1"]
    assert "* Compiled executabl" in log["1.2"]


def test_muda():
    log = changelogs.get("muda")
    assert "Initial public relea" in log["0.1.0"]
    assert "This is a minor bug-" in log["0.1.1"]
    assert "This ia a minor bug-" in log["0.1.2"]


def test_planetary_test_data():
    log = changelogs.get("planetary_test_data")
    assert "* First release on P" in log["0.1.0"]
    assert "* Fixed Python 3 com" in log["0.1.1"]
    assert "* Updated ``data.jso" in log["0.2.0"]
    assert "* Rewritten to be dr" in log["0.3.0"]
    assert "* Updated data.json " in log["0.3.1"]
    assert "* Added 2m132591087c" in log["0.3.2"]
    assert "* Added 0047MH000011" in log["0.3.3"]


def test_planetaryimage():
    log = changelogs.get("planetaryimage")
    assert "* First release on P" in log["0.1.0"]
    assert "* Improved support f" in log["0.2.0"]
    assert "* Added support for " in log["0.3.0"]
    assert "* Added basic suppor" in log["0.4.0"]
    assert "* Fixes to saving PD" in log["0.4.1"]


def test_planetpy():
    log = changelogs.get("planetpy")
    assert "* First release on P" in log["0.1.0"]
    assert "* Add pdstools" in log["0.2.0"]


def test_plank():
    log = changelogs.get("plank")
    assert "Unreleased" in log["0.0.1"]


def test_planterbox():
    log = changelogs.get("planterbox")
    assert "- Initial complete r" in log["0.1"]
    assert "- Rearrange feature " in log["0.2"]
    assert "- Bugfix release for" in log["0.2.1"]
    assert "- More bugfixes for " in log["0.2.2"]
    assert "- Treat lines beginn" in log["0.3"]
    assert "- Add planterbox con" in log["0.4"]
    assert "- Add after error an" in log["0.4.1"]


def test_planterbox_webdriver():
    log = changelogs.get("planterbox_webdriver")
    assert "- Add support for sc" in log["0.3"]
    assert "- Temporarily move b" in log["0.3.1"]
    assert "- Improve reliabilit" in log["0.3.2"]
    assert "- Report errors from" in log["0.3.3"]


def test_plaster():
    log = changelogs.get("plaster")
    assert "- Initial release." in log["0.1"]
    assert "- Allow ``config_uri" in log["0.2"]


def test_platocdp_newsportlet():
    log = changelogs.get("platocdp_newsportlet")
    assert "- Initial package ge" in log["1.0a1"]
    assert "- Nothing changed ye" in log["1.0a2"]


def test_platocdp_timesheet():
    log = changelogs.get("platocdp_timesheet")
    assert "- Initial package ge" in log["0.1"]


def test_platter():
    log = changelogs.get("platter")
    assert "(no codename yet, re" in log["1.0"]


def test_play_scraper():
    log = changelogs.get("play_scraper")
    assert "* Added urljoin impo" in log["0.1.1"]
    assert "* Price not availble" in log["0.1.10"]
    assert "* Arabic in Current " in log["0.1.11"]
    assert "* Bugfix: AGE_RANGE " in log["0.1.2"]
    assert "* Python3 urllib.par" in log["0.1.3"]
    assert "* Added number of re" in log["0.1.4"]
    assert "* Fixed App detail U" in log["0.1.5"]


def test_playdeliver():
    log = changelogs.get("playdeliver")
    assert "::" in log["1.1.0"]


def test_player():
    log = changelogs.get("player")
    assert "- Initial release" in log["0.1"]
    assert "- Added `layout` sub" in log["0.2"]
    assert "- Added `set_layout_" in log["0.3"]
    assert "- Added `player.layo" in log["0.4"]
    assert "- Use jinja2 for tem" in log["0.5"]
    assert "- Allow to use stand" in log["0.6"]
    assert "- Added python 2.6" in log["0.6.1"]


def test_playerdo():
    log = changelogs.get("playerdo")
    assert "* Initial release." in log["0.1"]
    assert "* Added support for " in log["0.2"]
    assert "* Fixed fatal packag" in log["0.3"]
    assert "* Added support for " in log["0.4"]
    assert "* Added support for " in log["0.5"]
    assert "* Fixed some Python " in log["0.5.1"]
    assert "* Fixed incorrect us" in log["0.5.2"]


def test_playerpiano():
    log = changelogs.get("playerpiano")


def test_playitagainsam():
    log = changelogs.get("playitagainsam")
    assert "* Initial release." in log["0.1.0"]
    assert "* Add options for au" in log["0.2.0"]
    assert "* Don't crash when g" in log["0.2.1"]
    assert "* Update for changes" in log["0.3.0"]
    assert "* Don't call get_def" in log["0.4.0"]
    assert "* Fixes for  Python " in log["0.5.0"]


def test_playsound():
    log = changelogs.get("playsound")
    assert "* Initial commit" in log["1.0.0"]
    assert "* Changed from using" in log["1.1.0"]
    assert "* Now uses   NSSound" in log["1.2.0"]
    assert "* Fixes bug that pre" in log["1.2.1"]


def test_plecost():
    log = changelogs.get("plecost")
    assert "Internal modificatio" in log["1.0.0"]


def test_pyladies():
    log = changelogs.get("pyladies")
    assert "Initial release of t" in log["1.0"]
    assert "* Released on PyPI" in log["2.0"]
    assert "* Fixed entry point," in log["2.0.2"]
    assert "* Removed the use of" in log["2.0.4"]


def test_pylama():
    log = changelogs.get("pylama")
    assert "2013-05-21  horneds" in log["0.3.5"]
    assert "2013-05-29  horneds" in log["1.0.0"]


def test_pylangacq():
    log = changelogs.get("pylangacq")
    assert "* first commit; set " in log["0.1"]
    assert "* new methods for cl" in log["0.2"]
    assert "* Class `Reader` can" in log["0.3"]
    assert "* New `number_of_utt" in log["0.4"]
    assert "* New `utterances()`" in log["0.5"]
    assert "* `cha_lines` optimi" in log["0.6"]
    assert "* Add `part_of_speec" in log["0.7"]


def test_pylapjv():
    log = changelogs.get("pylapjv")


def test_pylastfm():
    log = changelogs.get("pylastfm")
    assert "- Initial release" in log["0.1.1"]
    assert "- Removed following " in log["0.2.0"]


def test_pyldap():
    log = changelogs.get("pyldap")
    assert "dsml:" in log["2.0.0"]
    assert "- Fine-grained locki" in log["2.0.0pre05"]
    assert "LDAPObject.c:" in log["2.0.0pre06"]
    assert "ldap.schema:" in log["2.0.0pre07"]
    assert "Modified setup.py to" in log["2.0.0pre08"]
    assert "ldap.schema:" in log["2.0.0pre09"]
    assert "ldap.ldapobject:" in log["2.0.0pre10"]


def test_pyldavis():
    log = changelogs.get("pyldavis")
    assert "* First release on P" in log["1.0.0"]
    assert "* Fixes bug with Gra" in log["1.1.0"]
    assert "* Updates gensim log" in log["1.2.0"]
    assert "* Fixes gensim logic" in log["1.3.0"]
    assert "* Updates gensim and" in log["1.3.1"]
    assert "* Gensim prepare 25%" in log["1.3.2"]
    assert "* Gensim Python 2.x " in log["1.3.3"]


def test_pyleri():
    log = changelogs.get("pyleri")
    assert "support which can be used" in log["2016.03.07"]
    assert "Fixed export_c() t" in log["2016.07.02"]
    assert "Added export to Py" in log["2016.10.24"]
    assert "Fixed exporting To" in log["2016.10.25"]


def test_pylibacl():
    log = changelogs.get("pylibacl")
    assert "*released Sun, 21 Oc" in log["0.3"]
    assert "*released Sat, 28 Ju" in log["0.4"]
    assert "*released Sun, 27 De" in log["0.5"]
    assert "*released Sun, 13 Ma" in log["0.5.1"]
    assert "*released Sat, 24 Ma" in log["0.5.2"]
    assert "*released Thu, 30 Ap" in log["0.5.3"]


def test_pylibdmtx():
    log = changelogs.get("pylibdmtx")
    assert "* Initial release" in log["0.1.0"]
    assert "* Long description o" in log["0.1.1"]
    assert "* 1 Incorrect handli" in log["0.1.2"]
    assert "* 3 Convert images o" in log["0.1.3"]
    assert "* 5 Better handling " in log["0.1.4"]
    assert "* 7 Support older nu" in log["0.1.5"]
    assert "* 9 Check for empty " in log["0.1.6"]


def test_pylibfreenect2():
    log = changelogs.get("pylibfreenect2")
    assert "- Initial release" in log["0.1.0"]
    assert "- Fix installation i" in log["0.1.1"]


def test_pylibftdi():
    log = changelogs.get("pylibftdi")
    assert "* first release. Tes" in log["0.1"]
    assert "* support for FT232H" in log["0.10"]
    assert "* maintenance build " in log["0.10.1"]
    assert "* include examples s" in log["0.10.2"]
    assert "* lots more document" in log["0.10.3"]
    assert "* API changes" in log["0.11"]
    assert "* Optimisation on ac" in log["0.12"]


def test_pyliblinear():
    log = changelogs.get("pyliblinear")
    assert "*) Adjusted versioni" in log["1.96.0.dev2"]
    assert "*) fixed linkage err" in log["1.96.0.dev3"]
    assert "*) Added support for" in log["1.96.0.dev4"]
    assert "*) Upgrade to liblin" in log["2.1.0.dev1"]


def test_pyliblo():
    log = changelogs.get("pyliblo")
    assert "* Initial release." in log["0.1"]
    assert "* New and improved d" in log["0.10.0"]
    assert "* Minor improvements" in log["0.2"]
    assert "* Added class Server" in log["0.3"]
    assert "* Simplified the way" in log["0.5"]
    assert "* Fixed a stupid typ" in log["0.5.1"]
    assert "* Added support for " in log["0.6"]


def test_pylibmc():
    log = changelogs.get("pylibmc")
    assert "- Renamed the C modu" in log["0.4"]
    assert "- Fixed lots of memo" in log["0.5"]
    assert "- Added compatibilit" in log["0.6"]
    assert "- Restructured some " in log["0.7"]
    assert "- Pooling helpers ar" in log["0.8"]
    assert "- Added a ``get_stat" in log["0.9"]
    assert "- Lots of documentat" in log["1.0"]


def test_pylibrabbitmq():
    log = changelogs.get("pylibrabbitmq")
    assert ":release-date: NOT R" in log["0.0.1"]
    assert ":release-date: 2011-" in log["0.3.0"]
    assert ":release-date: 2011-" in log["0.4.0"]
    assert ":release-date: 2011-" in log["0.5.0"]


def test_pylibsass():
    log = changelogs.get("pylibsass")
    assert "Released June 23, 20" in log["0.1"]
    assert "Released June 26, 20" in log["0.1.3"]
    assert "Released June 27, 20" in log["0.1.4"]


def test_pylibscrypt():
    log = changelogs.get("pylibscrypt")
    assert "2014-5-2" in log["1.0.0"]
    assert "2014-5-3" in log["1.0.1"]
    assert "2014-5-3" in log["1.0.2"]
    assert "2014-5-5" in log["1.0.3"]
    assert "2014-5-8" in log["1.1.0"]
    assert "2014-5-12" in log["1.1.1"]
    assert "2014-5-12" in log["1.1.2"]


def test_qiita():
    log = changelogs.get("qiita")
    assert "* Fix setup.py: does" in log["0.1.1"]


def test_qiita_spots():
    log = changelogs.get("qiita_spots")
    assert "Initial alpha releas" in log["0.1.0"]
    assert "* Creating an empty " in log["0.2.0"]
    assert "* Users can now chan" in log["0.2.0dev"]


def test_qiniu_cli():
    log = changelogs.get("qiniu_cli")
    assert "* Initial Release" in log["0.1.0"]


def test_qipipe():
    log = changelogs.get("qipipe")
    assert "* Initial release fo" in log["1.1.1"]
    assert "* Support breast ima" in log["1.1.2"]
    assert "* Add dicom_helper m" in log["1.1.3"]
    assert "* Build xnat pipelin" in log["1.2.1"]
    assert "* Import new visits " in log["1.2.2"]
    assert "* Build registration" in log["1.2.3"]
    assert "* Integrate PK mappi" in log["2.1.1"]


def test_qiutil():
    log = changelogs.get("qiutil")
    assert "* Split out from qip" in log["1.1.1"]
    assert "* Remove bolus arriv" in log["1.1.2"]
    assert "* Fix qicp." in log["1.1.3"]
    assert "* Refactor dicom_hel" in log["1.2.1"]
    assert "* Add nested_default" in log["1.2.2"]
    assert "* Split out qixnat a" in log["2.1.1"]
    assert "* Propagate the appl" in log["2.1.10"]


def test_qixnat():
    log = changelogs.get("qixnat")
    assert "* Split out from qiu" in log["2.1.1"]
    assert "* Adapt for PyPI." in log["2.1.2"]
    assert "* Tweak distribution" in log["2.1.3"]
    assert "* Suggest Anaconda i" in log["2.1.4"]
    assert "* Fix qils." in log["2.1.5"]
    assert "* Fix qicp and qirm." in log["2.1.6"]
    assert "* Make the utilities" in log["3.1.1"]


def test_qllauncher():
    log = changelogs.get("qllauncher")
    assert "* Added ability to o" in log["0.6.1.1"]
    assert "* QuakeLive profile " in log["0.6.1.2"]
    assert "* Fixed bug when non" in log["0.6.1.3"]
    assert "* Fixed exception wh" in log["0.6.1.4"]
    assert "* Ability to obtain " in log["0.6.1.5"]
    assert "* Added user agent t" in log["0.6.1.6"]
    assert "* Refactored connect" in log["0.6.1.7"]


def test_qlutils():
    log = changelogs.get("qlutils")
    assert "* setup.py requireme" in log["0.1.0.10"]
    assert "* Added qllserver sc" in log["0.1.0.6"]
    assert "* Implemented argume" in log["0.1.0.9"]


def test_qmenuview():
    log = changelogs.get("qmenuview")
    assert "* First release on P" in log["0.1.0"]
    assert "* Fix getting parent" in log["0.1.1"]
    assert "* Fix removing all r" in log["0.1.4"]


def test_qonda():
    log = changelogs.get("qonda")
    assert "* First public relea" in log["0.4.0"]
    assert "* Add documentation " in log["0.4.1"]
    assert "* Definition of meta" in log["0.5.0"]
    assert "* Add new signal cur" in log["0.5.1"]
    assert "* PyQt5 compatibilit" in log["0.5.2"]
    assert "* Fix: Mapping of QL" in log["0.5.3"]
    assert "* Add SpinBox and De" in log["0.5.4"]


def test_qopen():
    log = changelogs.get("qopen")
    assert "* initial release" in log["1.0"]
    assert "* bugfix: energy env" in log["1.1"]
    assert "* bugfix: observed e" in log["1.2"]
    assert "* fix ObsPy deprecia" in log["1.3"]
    assert "* move some function" in log["1.4"]


def test_qpack():
    log = changelogs.get("qpack")
    assert "Added support for " in log["2016.10.02"]
    assert "Support for Byte-A" in log["2016.10.03"]
    assert "Added C module for" in log["2016.10.13"]
    assert "Fixed unicode bug " in log["2016.10.14"]
    assert "Removed p3c depend" in log["2016.10.17"]
    assert "Removed fallback p" in log["2016.10.18"]
    assert "Fixed Python2 bugs" in log["2016.10.19"]


def test_qpic():
    log = changelogs.get("qpic")
    assert "* First release on P" in log["1.0.0"]
    assert "* Convert README to " in log["1.0.1"]
    assert "* Fix Python3 unicod" in log["1.0.2"]


def test_qrcode():
    log = changelogs.get("qrcode")
    assert "* Added a ``qr`` scr" in log["2.1"]
    assert "* Fixed tty output t" in log["2.2"]
    assert "* When adding data, " in log["2.3"]
    assert "* Encode unicode to " in log["2.3.1"]
    assert "* Use a pluggable ba" in log["2.4"]
    assert "* Fix a packaging is" in log["2.4.1"]
    assert "* Added a ``show`` m" in log["2.4.2"]


def test_qstk():
    log = changelogs.get("qstk")
    assert "* Cleaning up the re" in log["0.2.3"]
    assert "* Moved from distuti" in log["0.2.4"]
    assert "* Adding validation " in log["0.2.5"]
    assert "* Remove CVXOPT from" in log["0.2.6"]


def test_qstring():
    log = changelogs.get("qstring")
    assert "- Initial public rel" in log["0.1.0"]
    assert "- Changed ``qstring." in log["0.2.0"]


def test_qt_binder():
    log = changelogs.get("qt_binder")
    assert "``qt_binder`` is born!" in log["0.1"]
    assert "Fixes" in log["0.1.1"]
    assert "Fixes" in log["0.1.2"]
    assert "Features" in log["0.2"]


def test_sijax():
    log = changelogs.get("sijax")
    assert "Huge reorganization " in log["0.2.0"]
    assert "TypeError exceptions" in log["0.2.1"]
    assert "TypeError exceptions" in log["0.2.2"]
    assert "Adds jQuery 1.6 supp" in log["0.2.3"]
    assert "jQuery 1.6 fix for t" in log["0.2.4"]
    assert "Minor documentation " in log["0.2.5"]
    assert "Introduces Python 3 " in log["0.3.0"]


def test_silentdune_client():
    log = changelogs.get("silentdune_client")


def test_silex():
    log = changelogs.get("silex")
    assert "- Prepare first rele" in log["0.1.0"]


def test_silly_content_generator():
    log = changelogs.get("silly_content_generator")
    assert "- Initial release" in log["1.0"]
    assert "-" in log["1.1"]


def test_silp():
    log = changelogs.get("silp")
    assert "First version, can d" in log["0.1.0"]
    assert "- Better control wit" in log["0.2.0"]
    assert "- Bugfix with the .m" in log["0.2.2"]
    assert "to change the langua" in log["0.2.3"]
    assert "Fix the wrong `impor" in log["0.2.4"]
    assert "Add support for YML " in log["0.2.5"]
    assert "Add simple plugin su" in log["0.3.1"]


def test_silva_app_document():
    log = changelogs.get("silva_app_document")
    assert "* Update and import " in log["3.0"]
    assert "* Extends ``IDocumen" in log["3.0.1"]
    assert "* Update tests to be" in log["3.0.2"]
    assert "* ..." in log["3.0.3"]
    assert "* Initial release." in log["3.0b1"]
    assert "* Update API to Silv" in log["3.0c1"]


def test_silva_app_forest():
    log = changelogs.get("silva_app_forest")
    assert "* Add events upon ac" in log["3.0"]
    assert "* Add an interface `" in log["3.0.1"]
    assert "* ..." in log["3.0.2"]
    assert "* Initial release." in log["3.0c1"]


def test_silva_app_mediacontent():
    log = changelogs.get("silva_app_mediacontent")
    assert "- Official release" in log["1.0"]
    assert "- Initial release" in log["1.0b1"]
    assert "- Add a block for ``" in log["3.0"]
    assert "- Add support for XM" in log["3.0.1"]
    assert "- Update tests to be" in log["3.0.2"]
    assert "- ..." in log["3.0.3"]


def test_silva_app_news():
    log = changelogs.get("silva_app_news")
    assert "- A news publication" in log["3.0"]
    assert "- Update Silva XML i" in log["3.0.1"]
    assert "- Force date index t" in log["3.0.2"]
    assert "- An agenda filter c" in log["3.0.3"]
    assert "- Change how the dat" in log["3.0.4"]
    assert "- ..." in log["3.0.5"]
    assert "- Initial version as" in log["3.0b1"]


def test_silva_app_page():
    log = changelogs.get("silva_app_page")
    assert "- Update Silva XML i" in log["3.0"]
    assert "- Update Silva XML i" in log["3.0.1"]
    assert "- Update tests." in log["3.0.2"]
    assert "- Update tests to be" in log["3.0.3"]
    assert "- Change how the dat" in log["3.0.4"]
    assert "- ..." in log["3.0.5"]
    assert "- Initial release of" in log["3.0c1"]


def test_silva_app_photogallery():
    log = changelogs.get("silva_app_photogallery")
    assert "* Initial release." in log["1.0"]
    assert "* ..." in log["1.1"]


def test_silva_app_redirectlink():
    log = changelogs.get("silva_app_redirectlink")
    assert "- Initial release." in log["1.0"]
    assert "- Compatibility fixe" in log["1.1"]
    assert "- Mark Silva Redirec" in log["3.0"]
    assert "- ..." in log["3.0.1"]
    assert "- Update code for Zo" in log["3.0b1"]
    assert "- Update API to Silv" in log["3.0c1"]


def test_silva_app_shorturl():
    log = changelogs.get("silva_app_shorturl")
    assert "* Initial release" in log["3.0"]
    assert "* Update API for nam" in log["3.0.1"]
    assert "* Fix bugs when serv" in log["3.0.2"]
    assert "* ..." in log["3.0.3"]


def test_silva_app_sitemap():
    log = changelogs.get("silva_app_sitemap")
    assert "* Initial release" in log["1.0"]
    assert "* ..." in log["1.0.1"]


def test_silva_app_subscriptions():
    log = changelogs.get("silva_app_subscriptions")
    assert "* Initial after spli" in log["1.0"]
    assert "* Change widget used" in log["1.1"]
    assert "* Improve tests." in log["3.0"]
    assert "* Add a link in the " in log["3.0.1"]
    assert "* Modify public form" in log["3.0.2"]
    assert "* Make possible to c" in log["3.0.3"]
    assert "* ..." in log["3.0.4"]


def test_silva_batch():
    log = changelogs.get("silva_batch")
    assert "- Initial release" in log["1.0"]
    assert "- Update traversing " in log["1.1"]
    assert "- ..." in log["1.2"]


def test_silva_captcha():
    log = changelogs.get("silva_captcha")
    assert "* Initial release." in log["1.0"]
    assert "* Fix broken extensi" in log["1.0.1"]
    assert "* Add a ``validate``" in log["1.1"]
    assert "* Added Formulator f" in log["1.2"]
    assert "* Fix tests if Gener" in log["1.2.1"]
    assert "* Don't rely anymore" in log["1.3"]
    assert "* Update generated `" in log["1.3.1"]


def test_silva_core_cache():
    log = changelogs.get("silva_core_cache")
    assert "* Initial release." in log["2.3"]
    assert "* Fix cookie path fo" in log["2.3.1"]
    assert "* Ensure caching key" in log["2.3.2"]
    assert "* Add a memcache sli" in log["3.0"]
    assert "* Session cookie use" in log["3.0.1"]
    assert "* Session cookie now" in log["3.0.2"]
    assert "* ..." in log["3.0.3"]


def test_silva_core_conf():
    log = changelogs.get("silva_core_conf")
    assert "* Initial release." in log["2.2a1"]
    assert "* Tag system extensi" in log["2.2a2"]
    assert "* We now use silva.c" in log["2.2b1"]
    assert "* Remove martian sup" in log["2.3"]
    assert "* Directive are now " in log["2.3.1"]
    assert "* define interface t" in log["2.3b1"]
    assert "* Use ``ISilvaNameCh" in log["3.0"]


def test_ticketus():
    log = changelogs.get("ticketus")
    assert "* Import scripts for" in log["0.5beta"]
    assert "* Added mail gateway" in log["0.6.0"]


def test_tickeys():
    log = changelogs.get("tickeys")
    assert "1.加入changlog" in log["0.1.0a4"]
    assert "1.修改配色，使风格大致与mac版相同" in log["0.1.1a5"]
    assert "1.修改键盘检测方法，支持更多键盘类型（" in log["0.1.1a6"]
    assert "1.更新键盘检测方法（测试中）" in log["0.1.2"]
    assert "1.修正因路径问题导致的配置无法正确显示" in log["0.1.3"]
    assert "1.打开程序后会出现气泡提醒" in log["0.1.4"]
    assert "1.实现真正后台化，启动后会隐藏窗口" in log["0.1.5"]


def test_ticktock():
    log = changelogs.get("ticktock")
    assert "* Initial release." in log["0.1"]
    assert "* Fixes sync() bug. " in log["0.1.1"]
    assert "* Removes duplicate " in log["0.1.2"]


def test_tictactoexxl():
    log = changelogs.get("tictactoexxl")
    assert "- Initial release." in log["1.0.0"]
    assert "- Bug Fixing." in log["1.0.1"]


def test_tiddlyweb():
    log = changelogs.get("tiddlyweb")
    assert "* First public relea" in log["0.5"]
    assert "* text store automat" in log["0.6"]
    assert "* add docs/CREDITS t" in log["0.7"]
    assert "* correct EncodeUTF8" in log["0.8"]
    assert "* Extensive adjustme" in log["0.9"]
    assert "* Fix a typo in a pl" in log["0.9.1"]
    assert "* When creating an i" in log["0.9.10"]


def test_tidehunter():
    log = changelogs.get("tidehunter")
    assert "Initial release" in log["0.1.0"]
    assert "Clean up setup.py " in log["0.1.1"]
    assert "Include CHANGES (c" in log["0.1.2"]
    assert "Use the great http" in log["0.1.3"]
    assert "Massive update to " in log["0.1.7"]
    assert "Added alias method" in log["0.1.8"]


def test_tif2geojson():
    log = changelogs.get("tif2geojson")
    assert "* Initial working ve" in log["0.1.0"]
    assert "* Fix module packagi" in log["0.1.1"]
    assert "* Fix error when dc:" in log["0.1.2"]
    assert "* Add a number of sa" in log["0.1.3"]
    assert "- Nothing changed ye" in log["0.1.4"]


def test_tifffile():
    log = changelogs.get("tifffile")
    assert "* First release on P" in log["0.1.0"]
    assert "* Add __version__ at" in log["0.2.0"]
    assert "* Install as a top-l" in log["0.3.0"]
    assert "* Do not require imp" in log["0.4.0"]
    assert "* Make tifffile a pa" in log["0.6.0"]


def test_tikapy():
    log = changelogs.get("tikapy")
    assert "Added" in log["0.1.1"]
    assert "Changed" in log["0.1.2"]
    assert "Added" in log["0.2.0"]
    assert "Fixed" in log["0.2.1"]


def test_tikz2pdf():
    log = changelogs.get("tikz2pdf")
    assert "* First release on P" in log["0.1.0"]


def test_tilde():
    log = changelogs.get("tilde")
    assert "[migrated to GitHub " in log["0.2.0"]
    assert "added single entry p" in log["0.2.1"]
    assert "switched to ASE to h" in log["0.2.2"]
    assert "major enhancements i" in log["0.2.3"]
    assert "data hierarchy is no" in log["0.2.4"]
    assert "bugfixes and minor e" in log["0.2.6"]
    assert "support of two backe" in log["0.2.7"]


def test_tilecloud_chain():
    log = changelogs.get("tilecloud_chain")
    assert "1. SQS config change" in log["0.5"]
    assert "it support ``filesys" in log["0.6"]
    assert "1. Support of defere" in log["0.7"]
    assert "1. Correct some erro" in log["0.8"]
    assert "1. Correct some erro" in log["0.9"]


def test_tilematrix():
    log = changelogs.get("tilematrix")
    assert "* basic functionalit" in log["0.0.1"]
    assert "* fixed wrong link t" in log["0.0.2"]
    assert "* rewrote io module" in log["0.0.3"]
    assert "* introduced ``Tile`" in log["0.0.4"]
    assert "* added Spherical Me" in log["0.1"]
    assert "* introduced handlin" in log["0.2"]
    assert "* fixed duplicate ti" in log["0.3"]


def test_tilestache():
    log = changelogs.get("tilestache")
    assert "- Made configuration" in log["1.1.0"]
    assert "- Fixed a bug in map" in log["1.1.1"]
    assert "- Refixed a bug in m" in log["1.1.2"]
    assert "- Found another mapn" in log["1.1.3"]
    assert "- Added new caches: " in log["1.10.0"]
    assert "- Fixed cache lifesp" in log["1.10.1"]
    assert "- Fixed TileStache.V" in log["1.10.2"]


def test_time2relax():
    log = changelogs.get("time2relax")
    assert "* First release on P" in log["0.1.0"]
    assert "* Python 3.3, 3.4, 3" in log["0.2.0"]


def test_timecode():
    log = changelogs.get("timecode")
    assert "defined in the previ" in log["0.2.0"]


def test_timecodes():
    log = changelogs.get("timecodes")
    assert "- Initial release." in log["0.0.1"]


def test_xlsx_streaming():
    log = changelogs.get("xlsx_streaming")
    assert "* First public versi" in log["0.1.0"]
    assert "* Add python 2.6 com" in log["0.2.0"]
    assert "* It is now possible" in log["0.3.0"]


def test_xlsx2csv():
    log = changelogs.get("xlsx2csv")
    assert "* xlsx to csv conver" in log["0.0"]
    assert "* better support for" in log["0.1"]
    assert "* no numFmt bugfix" in log["0.11"]
    assert "* fix last column em" in log["0.12"]
    assert "* sheet no bug fix" in log["0.13"]
    assert "* skip empty lines o" in log["0.131"]
    assert "* recursively conver" in log["0.14"]


def test_xlsxwriter():
    log = changelogs.get("xlsxwriter")
    assert "* First public relea" in log["0.0.1"]
    assert "* Added page setup m" in log["0.0.2"]
    assert "* Added page setup m" in log["0.0.3"]
    assert "* Added Python 3 sup" in log["0.0.4"]
    assert "* Added page setup m" in log["0.0.5"]
    assert "* Added page setup m" in log["0.0.6"]
    assert "* Added final page s" in log["0.0.7"]


def test_xlsxwriterchan():
    log = changelogs.get("xlsxwriterchan")
    assert "* First public relea" in log["0.0.1"]
    assert "* Added page setup m" in log["0.0.2"]
    assert "* Added page setup m" in log["0.0.3"]
    assert "* Added Python 3 sup" in log["0.0.4"]
    assert "* Added page setup m" in log["0.0.5"]
    assert "* Added page setup m" in log["0.0.6"]
    assert "* Added final page s" in log["0.0.7"]


def test_xlutils():
    log = changelogs.get("xlutils")
    assert "- initial public rel" in log["1.0.0"]
    assert "- link to the docume" in log["1.1.0"]
    assert "- prevented generati" in log["1.1.1"]
    assert "- add and implement " in log["1.2.0"]
    assert "- add extremely limi" in log["1.2.1"]
    assert "- fix bug that cause" in log["1.3.0"]
    assert "- In xlutils.styles," in log["1.3.1"]


def test_xm_charting():
    log = changelogs.get("xm_charting")
    assert "* Initial release" in log["0.1"]
    assert "* Small fixes." in log["0.2"]
    assert "* Style changes by M" in log["0.3"]
    assert "- Added z3c.autoincl" in log["0.4"]
    assert "- Moved to github: h" in log["0.5"]
    assert "- Nothing changed ye" in log["0.6"]


def test_xm_theme():
    log = changelogs.get("xm_theme")
    assert "- No history recorde" in log["0.2"]
    assert "- No history recorde" in log["0.3"]
    assert "- No history recorde" in log["0.4"]
    assert "- No history recorde" in log["0.5"]
    assert "- No history recorde" in log["0.6"]
    assert "- No history recorde" in log["0.7"]
    assert "- Use gradient image" in log["0.7.3"]


def test_xman():
    log = changelogs.get("xman")
    assert "- TBD" in log["0.0.0"]


def test_xmldataset():
    log = changelogs.get("xmldataset")
    assert "* First release on P" in log["0.1.0"]
    assert "* Minor updates to s" in log["0.1.1"]
    assert "* Minor updates to s" in log["0.1.2"]
    assert "* Minor updates to s" in log["0.1.3"]
    assert "* Added default opti" in log["0.1.4"]
    assert "* Added an option of" in log["0.1.5"]
    assert "* Updated the defaul" in log["0.1.6"]


def test_xmlenc():
    log = changelogs.get("xmlenc")
    assert "- Initial release." in log["0.1.0"]


def test_xmlformatter():
    log = changelogs.get("xmlformatter")


def test_xmljson():
    log = changelogs.get("xmljson")
    assert "- Two-way conversion" in log["0.1.0"]
    assert "- Convert ``true``, " in log["0.1.1"]
    assert "- Always use the ``d" in log["0.1.2"]
    assert "- Simplify ``{'p': {" in log["0.1.3"]
    assert "- Fix ``GData.etree(" in log["0.1.4"]
    assert "- Add the Yahoo_ XML" in log["0.1.5"]
    assert "- Add ``xml_fromstri" in log["0.1.6"]


def test_xmlpylighter():
    log = changelogs.get("xmlpylighter")
    assert "* first version" in log["0.1"]


def test_xmlr():
    log = changelogs.get("xmlr")
    assert "- Initial release" in log["0.1.0"]
    assert "- Bugfixes." in log["0.2.0"]
    assert "- Renaming from `xml" in log["0.3.0"]
    assert "- Made available on " in log["0.3.1"]


def test_xmlrpclibex():
    log = changelogs.get("xmlrpclibex")
    assert "- Initial commit" in log["0.1.0"]


def test_xmlrpcssl():
    log = changelogs.get("xmlrpcssl")


def test_xmlstats_py():
    log = changelogs.get("xmlstats_py")
    assert "Fixes:" in log["0.1.3"]
    assert "Fixes:" in log["0.1.4"]
    assert "Fixes:" in log["0.1.5"]


def test_xmltag():
    log = changelogs.get("xmltag")
    assert "Initial release" in log["1.0.0"]
    assert "- Add Layouts suppor" in log["1.1.0"]
    assert "- Escape content by " in log["1.3.0"]
    assert "- Remove unused impo" in log["1.3.1"]


def test_xmltodict():
    log = changelogs.get("xmltodict")
    assert "* Add force_list fea" in log["0.10.0"]
    assert "* Use defusedexpat i" in log["0.10.1"]
    assert "* Fixed defusedexpat" in log["0.10.2"]
    assert "* link to travis-ci " in log["0.2"]
    assert "* implemented postpr" in log["0.3"]
    assert "* 8 preprocessing ca" in log["0.4"]
    assert "* take all character" in log["0.4.1"]




