=======
History
=======

UNRELEASED
------------------

0.10.0 (2017-04-26)
-------------------
* Added support for GitHub release pages
* Added experimental support for git commit log parsing

0.9.0 (2017-04-05)
------------------

* Fix issue with custom parsing of packages with different case.
* Catch errors from launchpad.
* Add support for changing project name when switching vendors.
* Add support for finding URLs in the project description.
* Add support for ex code.google.com projects, now moved to github.
* Add support for parsing sourceforge repos.
* Added custom parser:
  - alembic
  - genshi
  - imapclient
  - mako
  - pyinotify
  - python-ldap
  - redis
  - uwsgi
  - pyaudio

0.8.0 (2017-03-29)
------------------

* added custom parser:
  - mysqlclient, thanks @alexkiro
* added custom launchpad backend, thanks to @alexkiro

0.7.0 (2017-03-06)
------------------

* added custom parsers
  - cheroot
  - pyparsing
  - gunicorn
  - sqlalchemy
  - djangorestframework
* tweaked the get_head function

0.6.1 (2017-02-08)
------------------

* added flake8 special parser

0.6.0 (2017-02-03)
------------------

* tweaked the parser, included tests for openpyxl

0.5.0 (2017-01-23)
------------------

* include docs-src as docs candidate

0.4.0 (2017-01-23)
------------------

* add better support for NPM packages

0.3.3 (2017-01-05)
------------------

* fix packagin error (hopefully)

0.3.2 (2017-01-05)
------------------

* use modules for custom imports, for packaging

0.3.1 (2017-01-03)
------------------

* the find_changelogs and get_urls functions now also return the repo URLs

0.3.0 (2017-01-03)
------------------

* allow to swap in the find_changelogs function

0.2.0 (2016-12-27)
------------------

* added support for rubygems
* added support for npm

0.1.0 (2016-12-19)
------------------

* First release on PyPI.
