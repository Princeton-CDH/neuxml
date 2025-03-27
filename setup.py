#!/usr/bin/env python
"""Setup.py for neuxml package"""
from distutils.command.build_py import build_py
from distutils.command.clean import clean
from distutils.command.sdist import sdist
from distutils.core import Command
import os
import sys
import shutil
from setuptools import setup, find_packages
import neuxml


class GenerateXmlCatalog(Command):
    '''Custom setup command to generate fresh catalog and schemas'''
    user_options = []

    def initialize_options(self):
        """init options"""
        pass

    def finalize_options(self):
        """finalize options"""
        pass

    def run(self):
        from neuxml.catalog import generate_catalog
        generate_catalog()


def generate_catalog_if_needed():
    # helper method to check if catalog is present, and generate if not
    if not os.path.exists(neuxml.XMLCATALOG_FILE):
        from neuxml.catalog import generate_catalog
        print("Cenerating XML catalog...")
        generate_catalog()



class CleanSchemaData(clean):
    """Custom cleanup command to delete build and schema files"""
    description = "Custom clean command; remove schema files and XML catalog"

    def run(self):
        # remove schema data and then do any other normal cleaning
        try:
            shutil.rmtree(neuxml.XMLCATALOG_DIR)
        except OSError:
            pass
        clean.run(self)


class BuildPyWithPly(build_py):
    """Use ply to generate parsetab and lextab modules."""

    def run(self):
        # importing this forces ply to generate parsetab/lextab
        import neuxml.xpath.core

        generate_catalog_if_needed()

        build_py.run(self)


class SdistWithCatalog(sdist):
    """Extend sdist command to ensure schema catalog is included."""

    def run(self):
        generate_catalog_if_needed()
        sdist.run(self)


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.12',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Text Processing :: Markup :: XML',
]

LONG_DESCRIPTION = None
try:
    # read the description if it's there
    with open('README.rst') as desc_f:
        LONG_DESCRIPTION = desc_f.read()
except:
    pass

dev_requirements = [
    'sphinx>=1.3.5',
    'coverage',
    'rdflib>=3.0',
    'mock',
    'pynose',
    'tox',
    'requests',
]
# NOTE: dev requirements should be duplicated in pip-dev-req.txt
# for generating documentation on readthedocs.org

# unittest2 should only be included for py2.6
if sys.version_info < (2, 7):
    dev_requirements.append('unittest2')


setup(
    cmdclass={
        'build_py': BuildPyWithPly,
        'clean': CleanSchemaData,
        'sdist': SdistWithCatalog,
        'xmlcatalog': GenerateXmlCatalog
    },

    name='neuxml',
    version=neuxml.__version__,
    author='Center for Digital Humanities at Princeton',
    author_email='cdhdevteam@princeton.edu',
    url='https://github.com/Princeton-CDH/neuxml',
    license='Apache License, Version 2.0',
    packages=find_packages(),

    setup_requires=[
        'ply>=3.8',
    ],
    install_requires=[
        'ply>=3.8',
        'lxml>=3.4',
        'six>=1.10',
    ],
    extras_require={
        'rdf': ['rdflib>=3.0'],
        'dev': dev_requirements
    },
    package_data={'neuxml': [
        # include schema catalog and all downloaded schemas in the package
        '%s/*' % neuxml.SCHEMA_DATA_DIR
    ]},
    description='XPath-based XML data binding',
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
)
