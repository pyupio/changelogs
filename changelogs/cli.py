# -*- coding: utf-8 -*-
import sys
import changelogs
from packaging.version import parse
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(
        description='bla'
    )
    parser.add_argument("package", help="echo the string you use here")
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")

    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    data = changelogs.get(args.package)
    for release in sorted(data.keys(), key=lambda v: parse(v), reverse=True):
        print(release)
        print(data[release])


if __name__ == "__main__":
    main()
