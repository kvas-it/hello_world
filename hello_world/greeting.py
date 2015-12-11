# -*- coding: utf-8 -*-

from __future__ import print_function

import yaml


def greet(name):
    """Print greeting for ``name``.

    :param str: name Name of the person to greet.
    """
    config = yaml.load('greeting: Hello, {}!\n')
    print(config['greeting'].format(name))
