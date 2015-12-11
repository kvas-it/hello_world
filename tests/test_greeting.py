# -*- coding: utf-8 -*-

from hello_world.greeting import greet


def test_greet(prints):
    greet('John')
    assert prints == [(('Hello, John!',), {})]
