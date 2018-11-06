"""
Setup.py for gtlb
"""

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='gtlb',
    version='0.0.2',
    description='',
    long_description='A CLI to open Gitlab project in a browser',
    url='https://github.com/danielwhatmuff/gtlb',
    author='Daniel Whatmuff',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='git gtlb gitlab cli open repo commandline browser',
    py_modules=["gtlb"],
    install_requires=['gitpython'],
    scripts=['bin/gtlb'],
)
