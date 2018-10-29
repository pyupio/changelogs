# -*- coding: utf-8 -*-
import re
from .changelogs import get, get_commit_log  # noqa: F401

"""
if os.environ.get("DEBUG", "") in ("TRUE", "True", "true"):
    DEBUG = True
    import logging
    logging.basicConfig(level=logging.DEBUG)
else:
    DEBUG = False
"""

__author__ = """Jannis Gebauer"""
__email__ = 'jay@pyup.io'
__version__ = '0.14.0'


url_re = re.compile(r"(https?://[^\s<>\"'\x7f-\xff]+)", re.IGNORECASE)
