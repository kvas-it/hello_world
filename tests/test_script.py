# -*- coding: utf-8 -*-

from hello_world.script import main


def test_no_args(prints, addarg):
    main()
    assert prints == [(('Hello, world!',), {})]


def test_one_arg(prints, addarg):
    addarg('Jude')
    main()
    assert prints == [(('Hello, Jude!',), {})]
