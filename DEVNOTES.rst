Developer Instructions
======================

Local installation
------------------

To install dependencies for your local check out of the code, run ``pip install``
in the ``neuxml`` directory (the use of `virtualenv`_ is recommended)::

    pip install -e .

.. _virtualenv: http://www.virtualenv.org/en/latest/


Unit tests and documentation
----------------------------

If you want to run unit tests or build sphinx documentation, you will also
need to install development dependencies::

    pip install -e . "neuxml[dev]"

To run all unit tests::

    # for normal development
    pytest

    # for continuous integration
    pytest --cov=neuxml --cov-report=xml

To run unit tests for a specific module, use syntax like this::

    pytest test/test_xpath.py

To generate sphinx documentation::

    cd doc
    make html

XML catalog
-----------

neuxml provides an `XML catalog <http://lxml.de/resolvers.html#xml-catalogs>`_
for loading schemas referenced by included XmlObject instances. 
The catalog and schemas are pulled from the web, and are included along
with the source code and in distributed releases. 

If you want to refresh the catalog by pulling new copies of the schemas
from the web, you can do so using the ``refresh_catalog`` function:

.. code-block:: python

    from neuxml.catalog import refresh_catalog
    refresh_catalog()

Running it without arguments will pull from the list of default schemas found
in that module, and store the schemas and catalog file in the subdirectory
``neuxml/schema_data``.

To specify other remote schema URLs and catalog locations, use the provided
keyword arguments ``xsd_schemas``, ``xmlcatalog_dir``, and ``xmlcatalog_file``.

Migration from ``eulxml``
-------------------------

A convenience script has been included under ``scripts/`` called
``migrate_eulxml.py`` to migrate your project from ``eulxml`` to ``neuxml``,
which will replace any usage of the package name in all ``.py`` files in the
passed directory and subdirectories. After upgrading to Python 3.12+ and
updating the package in your project's dependencies, you can run the script::

    python scripts/migrate_eulxml.py /path/to/your/project

In addition to renaming the package from ``eulxml`` to ``neuxml``, the usage
of indirect imports from ``neuxml.xmlmap`` has been removed, and definitions
must be imported directly from its submodules instead. The migration script
will also attempt to make these changes automatically.

For example, imports have changed from this style:

.. code-block:: python

    from neuxml import xmlmap

    xmlmap.XmlObject
    xmlmap.Field

to this style:

.. code-block:: python

    from neuxml.xmlmap import core, fields

    core.XmlObject
    fields.Field

Class imports are also acceptable (e.g. ``from neuxml.xmlmap.core import
XmlObject``).
