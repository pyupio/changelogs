# -*- coding: utf-8 -*-
import os
import re
from requests import Session
from .changelogs import get, get_commit_log

"""
if os.environ.get("DEBUG", "") in ("TRUE", "True", "true"):
    DEBUG = True
    import logging
    logging.basicConfig(level=logging.DEBUG)
else:
    DEBUG = False
"""

__author__ = """pyup.io"""
__email__ = 'support@pyup.io'
__version__ = '0.15.0-dev'


url_re = re.compile(r"(https?://[^\s<>\"'\x7f-\xff]+)", re.IGNORECASE)
