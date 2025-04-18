# file neuxml/xmlmap/__init__.py
#
#   Copyright 2010,2011 Emory University Libraries
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Map XML to Python objects.

This package facilitates access to XML data using common Pythonic idioms. XML
nodes map to Python attributes using XPath expressions.

For developer convenience this package is divided into submodules. Users
should import the names from submodules. This package exports
the following names:
 * core.XmlObject -- a base class for XML-Python mapping objects
 * core.parseUri and core.parseString -- parse a URI or string into an xml node with
   XPath methods that xmlmap depends on
 * core.load_xmlobject_from_string and core.load_xmlobject_from_file -- parse a string
   or file directly into an XmlObject
 * fields.NodeField and fields.NodeListField -- field classes for mapping relative
   xml nodes to other XmlObjects
 * fields.StringField and fields.StringListField -- field classes for mapping xml
   nodes to Python strings
 * fields.IntegerField and fields.IntegerListField -- field classes for mapping xml
   nodes to Python integers

"""
