# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='ninepatch',
    version='0.1.19',
    author='Thomas Schüßler',
    author_email='vindolin@gmail.com',
    packages=['ninepatch'],
    scripts=['bin/ninepatch', 'bin/ninepatch_viewer'],
    url='https://github.com/vindolin/ninepatch',
    license=open('LICENSE').read(),
    description='Slice and scale 9-patch images',
    long_description=open('README.rst').read(),
    install_requires=['pillow'],
    include_package_data=True,
    data_files=[('', ['LICENSE', 'README.rst'])],
)
