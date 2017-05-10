# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


def get_urls(releases, **kwargs):
    # graphene has a releases changelog
    return [
        "https://api.github.com/repos/graphql-python/graphene/releases",
    ], set()
