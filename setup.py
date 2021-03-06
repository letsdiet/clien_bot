# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "clien_bot"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Clien notification bot",
    author_email="",
    url="",
    keywords=["Swagger", "Clien notification bot"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['clien_bot=clien_bot.__main__:main']},
    long_description="""\
    Description...
    """
)

