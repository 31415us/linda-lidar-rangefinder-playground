#! /usr/bin/python

from setuptools import setup

args = dict(
        name='linda',
        version='0.1',
        description='lidar rangefinder playground',
        packages=['linda'],
        install_requires=[],
        author='Pius von Daeniken',
        url='https://github.com/31415us/linda-lidar-rangefinder-playground'
)

setup(**args)
