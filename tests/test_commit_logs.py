# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import pytest

from changelogs import get_commit_log

# Todo: find a way to make this test run on travis
"""
@pytest.fixture(autouse=True)
@pytest.mark.usefixtures('betamax_session')
def record(monkeypatch, betamax_session):
    def session():
        return betamax_session
    monkeypatch.setattr("changelogs.changelogs.Session", session)


def test_changelogs():
    log, raw_log = get_commit_log("changelogs")
    assert 'Correct time traveling changelog. [Alexandru Chirila]' in log['0.9.0']
    assert 'Bump version: 0.2.0 → 0.3.0' in log['0.3.0']

    assert 'fcafefa4380a03135745f5e306577ff2446130bb' in raw_log
    assert 'added test dependencies' in raw_log
    assert 'initial release from pyup.io' in raw_log
"""
