# -*- coding: utf-8 -*-
import os
from requests import Session
from .changelogs import get

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
__version__ = '0.3.1'
