# -*- coding: utf-8 -*-
# Shared test configuration.

from __future__ import print_function

import pytest


@pytest.fixture
def prints(monkeypatch):
    """Capture prints into a list."""
    prints = []
    def save_print(*args, **kw):
        prints.append((args, kw))

    if hasattr(__builtins__, 'get'):
        monkeypatch.setitem(__builtins__, 'print', save_print)
    else:
        # For pypy we need to monkeypatch differently.
        monkeypatch.setattr(__builtins__, 'print', save_print)

    return prints


@pytest.fixture
def addarg(monkeypatch):
    """Add things to sys.argv."""
    fake_argv = ['hello']
    def addarg(arg):
        fake_argv.append(arg)

    monkeypatch.setattr('sys.argv', fake_argv)

    return addarg



