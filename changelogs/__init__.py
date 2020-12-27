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

__author__ = """pyup.io"""
__email__ = 'support@pyup.io'
__version__ = '0.15.0'


url_re = re.compile(r"(https?://[^\s<>\"'\x7f-\xff]+)", re.IGNORECASE)
