======
neuxml
======

**package**
  .. image:: https://img.shields.io/pypi/v/neuxml.svg
    :target: https://pypi.python.org/pypi/neuxml
    :alt: PyPI

  .. image:: https://img.shields.io/github/license/Princeton-CDH/neuxml.svg
    :alt: License

  .. image:: https://img.shields.io/pypi/dm/neuxml.svg
    :alt: PyPI downloads

neuxml is a `Python <http://www.python.org/>`_ module that provides
utilities and classes for interacting with XML that allow the
definition of re-usable XML objects that can be accessed, updated and
created as standard Python types.

**neuxml.xpath** provides functions and classes for parsing XPath
expressions using `PLY <http://www.dabeaz.com/ply/>`_.

**neuxml.xmlmap** makes it easier to map XML to Python objects in a
nicer, more pythonic and object-oriented way than typical DOM access
usually provides.  XML can be read, modified, and even created from
scratch (in cases where the configured XPath is simple enough to
determine the nodes that should be constructed).

Dependencies
============

**neuxml** depends on `PLY <http://www.dabeaz.com/ply/>`_ and `lxml
<http://lxml.de/>`_.


Contact Information
===================

**eulxml** was created by the `Center for Digital Humanities at Princeton <https://cdh.princeton.edu/>`_.

cdhdevteam@princeton.edu


License
=======
**neuxml** is distributed under the Apache 2.0 License.


Development History
===================

This codebase was forked from a package called **eulxml**, originally developed
by Emory University Libraries. To see and interact with the full development
history of **eulxml**, see `eulxml <https://github.com/emory-libraries/eulxml>`_.

Developer notes
===============

neuxml provides an `XML catalog <http://lxml.de/resolvers.html#xml-catalogs>`_
for loading schemas referenced by included XmlObject instances. `Requests <https://github.com/kennethreitz/requests>`_ is required for downloading schemas, but it is not a dependency of neuxml. The
catalog and schemas will be included in distributed releases, but if you
want to use the catalog when installing directly from GitHub you can
use a normal pip install and then run::

  python -c 'from neuxml.catalog import generate_catalog; generate_catalog()'


To install dependencies for your local check out of the code, run ``pip install``
in the ``neuxml`` directory (the use of `virtualenv`_ is recommended)::

    pip install -e .

.. _virtualenv: http://www.virtualenv.org/en/latest/

If you want to run unit tests or build sphinx documentation, you will also
need to install development dependencies::

    pip install -e . "neuxml[dev]"

To run all unit tests::

    nosetests   # for normal development
    nosetests --with-coverage --cover-package=neuxml --cover-xml --with-xunit   # for continuous integration

To run unit tests for a specific module, use syntax like this::

    nosetests test/test_xpath.py


To generate sphinx documentation::

    cd doc
    make html

Migration from ``eulxml``
-------------------------

After updating your project's dependencies to point at the new package name,
you can run this one-line shell script to find and replace every instance of
``eulxml`` with ``neuxml`` in all ``.py`` files in the current working
directory and subdirectories.

On MacOS:

.. code-block:: shell

   find . -name '*.py' -print0 | xargs -0 sed -i '' -e 's/eulxml/neuxml/g'


Or on other Unix-based operating systems:

.. code-block:: shell

   find . -name '*.py' -print0 | xargs -0 sed -i 's/eulxml/neuxml/g'
