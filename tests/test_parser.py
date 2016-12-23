# -*- coding: utf-8 -*-
import pytest
from changelogs.parser import get_head


def test_get_head():
    assert "1.1.2" == get_head("django", "Django 1.1.2 release notes", ["1.1.2"])
    assert "4.5.0" == get_head("mayavi", "Mayavi 4.5.0", ["4.5.0"])
