#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import memcache

setup(name="pymemcached",
      version=memcache.__version__,
      description="Python2.6+ and Python3.1+ compatible pure python memcached client",
      long_description=open("README.rst").read(),
      author="Evan Martin",
      author_email="martine@danga.com",
      maintainer="Eren Guven",
      maintainer_email="erenguven0@gmail.com",
      url="https://github.com/eguven/pymemcached",
      download_url="https://github.com/eguven/pymemcached/downloads",
      py_modules=["memcache"],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ])

