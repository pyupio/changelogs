# -*- coding: utf-8 -*-
import changelogs
from packaging.version import parse
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(
        description='A changelog finder and parser for packages available on pypi, npm and rubygems.'
    )
    parser.add_argument("package", help="package name")
    parser.add_argument("vendor", help="vendor (pypi, npm, gem)", default="pypi", nargs='?')
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-c", "--commits", help="",
                        action="store_true")
    parser.add_argument("-r", "--reverse", help="list changelogs from older to newer", action="store_false")
    parser.add_argument("-n", help="only show the n first results (defaults to all)", type=int)

    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    if args.commits:
        data, raw_log = changelogs.get_commit_log(args.package, vendor=args.vendor)
    else:
        data = changelogs.get(args.package, vendor=args.vendor)

    for release in sorted(data.keys(), key=lambda v: parse(v), reverse=args.reverse)[:args.n]:
        print(release)
        print(data[release])

    if not data and args.commits:
        print(raw_log)


if __name__ == "__main__":
    main()
