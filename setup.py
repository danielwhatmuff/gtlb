"""
Setup.py for g
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='g',
    version='0.0.1',
    description='',
    long_description='A CLI to open Gitlab project in a browser',
    url='https://github.com/danielwhatmuff/g',
    author='Daniel Whatmuff',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='git gitlab cli open repo commandline browser',
    py_modules=["g"],
    install_requires=['gitpython'],
    scripts=['bin/g'],
)
