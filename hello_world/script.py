# -*- coding: utf-8 -*-

import sys

from .greeting import greet


def main():
    """Greet ``argv[1]`` or world."""
    if len(sys.argv) > 1:
        greet(sys.argv[1])
    else:
        greet('world')
