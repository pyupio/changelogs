.. image:: https://img.shields.io/pypi/v/changelogs.svg
        :target: https://pypi.python.org/pypi/changelogs

.. image:: https://img.shields.io/travis/pyupio/changelogs.svg
        :target: https://travis-ci.org/pyupio/changelogs

.. image:: https://readthedocs.org/projects/changelogs/badge/?version=latest
        :target: https://changelogs.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/pyupio/changelogs/shield.svg
     :target: https://pyup.io/repos/github/pyupio/changelogs/
     :alt: Updates

A changelog finder and parser with command line interface for packages available on pypi, npm and rubygems. Originally developed for pyup.io_.

.. _pyup.io: https://pyup.io/


************
Installation
************

To install changelogs, run this command in your terminal:

.. code-block:: console

    $ pip install changelogs

*****
Usage
*****

To use changelogs in a Python project::

    import changelogs

    logs = changelogs.get("flask")
    logs = changelogs.get("babel", vendor="npm")
    logs = changelogs.get("bundler", vendor="npm")


Or, from the command line::

    changelogs flask
    changelogs babel npm
    changelogs bundler gem

If you are on macOS, you can chain the `open` command::

    changelogs babel npm >> babel.log && open babel.log


*****
About
*****

When trying to get a changelog for a given package, there are a bunch of problems:

- There is no central place to store a changelog. If a project has a changelog, it's most likely somewhere in the git repo at all kinds of different places. This makes it hard to find.
- The package index meta data often has no direct link to the git repo. This makes the repo hard to find.
- There is no changelog standard. Everyone uses a different approach. This makes it hard to parse.

This project is trying to solve this by:

- first querying the package vendor for package meta data like the homapage or docs URL.
- if the meta data doesn't contain a valid URL to a repo, visit all available URLs and scrape them to find one.
- if there is a valid repo URL, visit the repo and look for possible changelogs like `Changes.txt`, `NEWS.md` or `history.rst`.
- fetch the content and somewhat try to parse it.


