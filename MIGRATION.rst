Migration from ``eulxml``
-------------------------

A convenience script called ``migrate-eulxml`` has been included in order
to migrate your project from ``eulxml`` to ``neuxml``, which will replace
any usage of the package name in all ``.py`` files in the passed directory
and subdirectories. After upgrading to Python 3.12+ and installing the
updated package, you can run the script::

    migrate-eulxml /path/to/your/project

Or you can run the script directly without installing the package::

    python neuxml/utils/migrate_eulxml.py /path/to/your/project

In addition to renaming the package from ``eulxml`` to ``neuxml``, the usage
of indirect imports from ``neuxml.xmlmap`` has been removed, and definitions
must be imported directly from its submodules instead. The migration script
will also attempt to make these changes automatically, but may not work in
all cases, so be sure to check your imports manually as well.

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

Class and function imports are also acceptable (e.g. ``from neuxml.xmlmap.core
import XmlObject``).

----

If you would like to automatically replace all instances of ``eulxml`` with
``neuxml`` but otherwise complete the import migration manually, you may use
the following one-line shell script. 

On MacOS:

.. code-block:: shell

   find . -name '*.py' -print0 | xargs -0 sed -i '' -e 's/eulxml/neuxml/g'

Or on other Unix-based operating systems:

.. code-block:: shell

   find . -name '*.py' -print0 | xargs -0 sed -i 's/eulxml/neuxml/g'
