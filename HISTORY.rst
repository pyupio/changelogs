=======
History
=======

0.15.0 (2020-12-27)
-------------------
* Removed support for Python 2.7, 3.4 and 3.5
* Added support for Python 3.9
* Getting proper changelogs for beautifulsoup4 PyPi package again
* Getting proper changelogs for synapse PyPi package again
* Stopped using bumpversion
* Updated PyPi map.txt to reflect different packages changelogs location changes
* Fixed bug while processing domain-only URLs (#155)

0.14.0 (2018-01-9)
-------------------
* Added a pypi/map.txt file to add custom URLS more easily
* Added a bunch of custom URLS:
  - pytest-flake8
  - cornice.ext.swagger
  - python-social-core
  - python-social-auth
  - cx-oracle
  - plotnine
  - django-hijack
  - pyinvoke
  - gitpython
  - python-memcached
  - appenlight-client

0.13.0 (2018-01-9)
-------------------
* Added a bunch of custom parser:
  - robozilla
  - websocket-client
  - pep8-naming
  - py-trello
  - synapse
  - django-haystack
  - libsass
  - lazy-object-proxy

0.12.0 (2017-05-18)
-------------------
* Added a bunch of custom parser:
  - flake8
  - pyyaml
  - six
  - factory-boy
  - jinja2
  - docutils
  - sphinx-rtd-theme
  - whitenoise
  - numpy
  - beautifulsoup4
  - mccabe
  - django-braces
  - alabaster
  - cffi
  - django-coverage-plugin
  - newrelic
  - pandas
  - twine
  - pep8-naming
  - django-storages-redux
  - pbr


0.11.0 (2017-05-10)
-------------------

* The changelog finder now checks repo URLs if they contain the given project name. This should
  make it easier to identify false changelogs.
* Fixed a couple of internal errors on edge cases.
* Added custom parsers for:
  - graphene
  - beautifulsoup4

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
