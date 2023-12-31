#!/usr/bin/env python
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'jsonfield', 'VERSION')) as fp:
    version = fp.read().strip()

with open("README.rst") as fp:
    long_description = fp.read()

setup(
    name="django-jsonfield",
    version=version,
    description="JSONField for django models",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/adamchainz/django-jsonfield",
    author="Matthew Schinckel",
    author_email="matt@schinckel.net",
    maintainer="Adam Johnson",
    maintainer_email="me@adamj.eu",
    packages=[
        "jsonfield",
    ],
    include_package_data=True,
    test_suite='tests.main',
    install_requires=[
        'Django>=3.2',
    ],
    classifiers=[
        "Development Status :: 6 - Mature",
        'Framework :: Django',
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
