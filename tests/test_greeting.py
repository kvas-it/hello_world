# -*- coding: utf-8 -*-

from __future__ import print_function

import pytest

from hello_world.greeting import greet

@pytest.fixture
def prints(monkeypatch):
    """Fixture that captures prints."""
    prints = []
    def save_print(*args, **kw):
        prints.append((args, kw))

    if hasattr(__builtins__, 'get'):
        monkeypatch.setitem(__builtins__, 'print', save_print)
    else:
        # For pypy we need to monkeypatch differently.
        monkeypatch.setattr(__builtins__, 'print', save_print)

    return prints


def test_greet(prints):
    greet('John')
    assert prints == [(('Hello, John!',), {})]
