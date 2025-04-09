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


Developer instructions
======================

For development instructions and notes, see ``DEVNOTES.rst``.
