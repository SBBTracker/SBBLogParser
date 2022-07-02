#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

setup(
    name='sbblogparser',
    version='0.1.1c',
    description='A Storybook Brawl Log Parser',
    packages=find_packages(),
    install_requires=[
        'pygtail',
    ],
)
