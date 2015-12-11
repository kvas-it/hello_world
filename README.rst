Hello world
###########

.. image:: https://travis-ci.org/kvas-it/hello_world.svg?branch=master
    :target: https://travis-ci.org/kvas-it/hello_world

Example python project.

Requirements:
=============

- Python (2.7, 3.3, 3.4, 3.5, pypy),
- PyYAML.

Installation:
=============

**Hello world** can be installed using pip: ::

    $ pip install hello_world

Actually this doesn't work yet, so instead you will need to
clone the repository and use make: ::

    $ git clone https://github.com/kvas-it/hello_world.git
    $ cd hello_world
    $ make install

Quickstart
==========

Run hello_world as a script: ::

    $ hello_world <name>

Use hello_world as a library: ::

    from hello_world.greeting import greet

    greet('John')  # prints "Hello, John!"

Development
===========

Set up development environment: ::

    $ make devenv

This will create virtualenv and install this package there in development
mode (symlinking the sources instead of copying). It will also install
pytest and tox that are used for testing.

* Use ``make test`` to run the tests with default version of python
  (the version that is used to create the development environment).

* Use ``make testcov`` and ``make htmlcov`` to measure test coverage.

* Use ``make testall`` to run the tests for all supported python versions
  (2.7, 3.3, 3.4 and 3.5).

Please make sure ``make testall`` is successful before submitting
a pull request. Also try to not reduce test coverage without a good reason.
