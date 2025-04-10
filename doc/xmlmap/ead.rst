:mod:`neuxml.xmlmap.eadmap` - Encoded Archival Description (EAD)
=================================================================

.. module:: neuxml.xmlmap.eadmap

General Information
-------------------
The Encoded Archival Description (EAD) is a a standard xml format for encoding
finding aids.  For more information, please consult `the official Library of
Congress EAD site <http://www.loc.gov/ead/>`_.

This set of xml objects is an attempt to make the major fields of an EAD document
accessible for search and display.  It is by no means an exhaustive mapping of all
EAD elements in all their possible configurations.

Encoded Archival Description
----------------------------
`LOC documentation for EAD element <http://www.loc.gov/ead/tglib/elements/ead.html>`_

Nearly all fields in all EAD XmlObjects are mapped as
:class:`neuxml.xmlmap.XPathString` or :class:`neuxml.xmlmap.XPathStringList`,
except for custom EAD sub-objects, which are indicated where in use.

  .. autoclass:: neuxml.xmlmap.eadmap.EncodedArchivalDescription(node[, context])
      :members:

Archival Description
--------------------
`LOC documentation for EAD archdesc element <http://www.loc.gov/ead/tglib/elements/archdesc.html>`_

  .. autoclass:: neuxml.xmlmap.eadmap.ArchivalDescription(node[, context])
      :members:

Subordinate Components
----------------------
See also LOC documentation for `dsc element <http://www.loc.gov/ead/tglib/elements/dsc.html>`_ ,
`c (component) element <http://www.loc.gov/ead/tglib/elements/c.html>`_

  .. autoclass:: neuxml.xmlmap.eadmap.SubordinateComponents(node[, context])
      :members:

  .. autoclass:: neuxml.xmlmap.eadmap.Component(node[, context])
      :members:

Controlled Access Headings
--------------------------
`LOC Documentation for controlaccess element <http://www.loc.gov/ead/tglib/elements/controlaccess.html>`_

  .. autoclass:: neuxml.xmlmap.eadmap.ControlledAccessHeadings(node[, context])
      :members:

  .. autoclass:: neuxml.xmlmap.eadmap.Heading(node[, context])
      :members:

Index and Index Entry
---------------------
See also LOC Documentation for `index element <http://www.loc.gov/ead/tglib/elements/index-element.html>`_,
`indexentry element <http://www.loc.gov/ead/tglib/elements/indexentry.html>`_

  .. autoclass:: neuxml.xmlmap.eadmap.Index(node[, context])
      :members:

  .. autoclass:: neuxml.xmlmap.eadmap.IndexEntry(node[, context])
      :members:

File Description
-----------------
See also LOC Documentation for `filedesc element <http://www.loc.gov/ead/tglib/elements/filedesc.html>`_,
`publicationstmt element <http://www.loc.gov/ead/tglib/elements/publicationstmt.html>`_

  .. autoclass:: neuxml.xmlmap.eadmap.FileDescription(node[, context])
      :members:

  .. autoclass:: neuxml.xmlmap.eadmap.PublicationStatement(node[, context])
      :members:


Miscellaneous
-------------
See also LOC documentation for `did element <http://www.loc.gov/ead/tglib/elements/did.html>`_ ,
`container element <http://www.loc.gov/ead/tglib/elements/container.html>`_


  .. autoclass:: neuxml.xmlmap.eadmap.DescriptiveIdentification(node[, context])
      :members:

  .. autoclass:: neuxml.xmlmap.eadmap.Container(node[, context])
      :members:

  .. autoclass:: neuxml.xmlmap.eadmap.Section(node[, context])
      :members:

  .. autoclass:: neuxml.xmlmap.eadmap.Address(node[, context])
      :members:

  .. autoclass:: neuxml.xmlmap.eadmap.PointerGroup(node[, context])
      :members:

  .. autoclass:: neuxml.xmlmap.eadmap.Reference(node[, context])
      :members:

  .. autoclass:: neuxml.xmlmap.eadmap.ProfileDescription(dom_node[, context])
      :members:

  .. autoclass:: neuxml.xmlmap.eadmap.DigitalArchivalObject(dom_node[, context])
      :members:



