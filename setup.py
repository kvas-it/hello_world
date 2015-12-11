#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()


setup(
    name='hello_world',
    version='0.1.0',
    description='Example package',
    long_description=readme,
    author='Vasily Kuznetsov',
    author_email='kvas.it@gmail.com',
    url='https://github.com/kvas-it/hello_world',
    packages=find_packages('.'),
    include_package_data=True,
    install_requires=[
        'PyYAML'
    ],
    license='MIT',
    zip_safe=False,
    keywords='hello_world',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
