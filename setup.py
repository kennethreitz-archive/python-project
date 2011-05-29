#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from distutils.core import setup

import haystack


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    sys.exit()


required = []

setup(
    name='haystack',
    version = haystack.__version__,
    description = 'Hides all the needles.',
    long_description = open('README.rst').read()
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/python-project',
    packages= ['haystack',],
    install_requires=required,
    license='Apache',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
    ),
)
