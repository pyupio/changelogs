# -*- coding: utf-8 -*-
import sys
import changelogs
from packaging.version import parse
import argparse
import logging
import pydoc


def main():
    parser = argparse.ArgumentParser(
        description='bla'
    )
    parser.add_argument("package", help="package name")
    parser.add_argument("vendor", help="vendor (pypi, npm, gem)", default="pypi", nargs='?')
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-c", "--commits", help="",
                        action="store_true")

    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    if args.commits:
        data, raw_log = changelogs.get_commit_log(args.package, vendor=args.vendor)
    else:
        data = changelogs.get(args.package, vendor=args.vendor)

    if data:
        out = "".join(
            release + "\n" + data[release] + "\n"
            for release in sorted(data.keys(),
                                  key=lambda v: parse(v), reverse=True))
    elif args.commits:
        out = raw_log
    else:
        out = None

    if out is not None:
        pydoc.pager(out)


if __name__ == "__main__":
    main()
