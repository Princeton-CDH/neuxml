# file neuxml/xmlmap/teimap.py
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

from neuxml.xmlmap import core, fields

# TODO: generic/base tei xml object with common attributes?

TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"


class _TeiBase(core.XmlObject):
    """Common TEI namespace declarations, for use by all TEI XmlObject instances."""

    ROOT_NS = TEI_NAMESPACE
    ROOT_NAME = "tei"
    ROOT_NAMESPACES = {
        "tei": ROOT_NS,
        "xml": "http://www.w3.org/XML/1998/namespace",
    }


class TeiLine(_TeiBase):
    rend = fields.StringField("@rend")

    """set up indents for lines with @rend=indent plus some number. Handle default indent in css."""

    def indent(self):
        if self.rend.startswith("indent"):
            indentation = self.rend[len("indent") :]
            if indentation:
                return int(indentation)
            else:
                return 0


class TeiLineGroup(_TeiBase):
    head = fields.StringField("tei:head")
    linegroup = fields.NodeListField("tei:lg", "self")
    line = fields.NodeListField("tei:l", TeiLine)


class TeiQuote(_TeiBase):
    line = fields.NodeListField("tei:l", TeiLine)
    linegroup = fields.NodeListField("tei:lg", TeiLineGroup)


class TeiEpigraph(_TeiBase):
    quote = fields.NodeListField(
        "tei:q|tei:quote|tei:cit/tei:q|tei:cit/tei:quote", TeiQuote
    )
    bibl = fields.StringField("tei:bibl")


class TeiDiv(_TeiBase):
    id = fields.StringField("@xml:id")
    type = fields.StringField("@type")
    author = fields.StringField("tei:docAuthor/tei:name/tei:choice/tei:sic")
    docauthor = fields.StringField("tei:docAuthor")
    title = fields.StringField("tei:head[1]")  # easy access to FIRST head
    title_list = fields.StringListField(
        "tei:head"
    )  # access to all heads when there are multiple
    text = fields.StringField(
        "."
    )  # short-hand mapping for full text of a div (e.g., for short divs)
    linegroup = fields.NodeListField("tei:lg", TeiLineGroup)
    div = fields.NodeListField("tei:div", "self")
    byline = fields.StringField("tei:byline")
    epigraph = fields.NodeListField("tei:epigraph", TeiEpigraph)
    p = fields.StringListField("tei:p")
    q = fields.StringListField("tei:q")
    quote = fields.StringListField("tei:quote")
    floatingText = fields.NodeListField("tei:floatingText/tei:body/tei:div", "self")


class TeiFloatingText(_TeiBase):
    head = fields.StringField("./tei:body/tei:head")
    line_group = fields.NodeListField(".//tei:lg", TeiLineGroup)
    line = fields.NodeListField(".//tei:l", TeiLine)


# note: not currently mapped to any of the existing tei objects...  where to add?
class TeiFigure(_TeiBase):
    # entity      = fields.StringField("@entity") #not used in P5
    # TODO: ana should be a more generic attribute, common to many elements...
    ana = fields.StringField(
        "@ana"
    )  # FIXME: how to split on spaces? should be a list...
    head = fields.StringField("tei:head")
    description = fields.StringField("tei:figDesc")
    entity = fields.StringField("tei:graphic/@url")  # graphic replaces entity in p5.
    floatingText = fields.NodeListField("tei:floatingText", TeiFloatingText)


# currently not mapped... should it be mapped by default? at what level?
class TeiInterp(_TeiBase):
    ROOT_NAME = "interp"
    id = fields.StringField("@xml:id")
    value = fields.StringField(".")


class TeiSection(_TeiBase):
    # top-level sections -- front/body/back
    div = fields.NodeListField("tei:div", TeiDiv)
    all_figures = fields.NodeListField(".//tei:figure", TeiFigure)


class TeiInterpGroup(_TeiBase):
    ROOT_NAME = "interpGrp"
    type = fields.StringField("@type")
    interp = fields.NodeListField("tei:interp", TeiInterp)


class TeiName(_TeiBase):
    type = fields.StringField("@person")
    reg = fields.StringField("tei:choice/tei:reg")
    "regularized value for a name"
    value = fields.StringField("tei:choice/tei:sic")
    "name as displayed in the text"


class TeiHeader(_TeiBase):
    """xmlmap object for a TEI (Text Encoding Initiative) header"""

    title = fields.StringField("tei:fileDesc/tei:titleStmt/tei:title")
    author_list = fields.NodeListField(
        "tei:fileDesc/tei:titleStmt/tei:author/tei:name", TeiName
    )
    editor_list = fields.NodeListField(
        "tei:fileDesc/tei:titleStmt/tei:editor/tei:name", TeiName
    )
    publisher = fields.StringField("tei:fileDesc/tei:publicationStmt/tei:publisher")
    publication_date = fields.StringField("tei:fileDesc/tei:publicationStmt/tei:date")
    availability = fields.StringField(
        "tei:fileDesc/tei:publicationStmt/tei:availability"
    )
    source_description = fields.StringField("tei:fileDesc/tei:sourceDesc")
    series_statement = fields.StringField("tei:fileDesc/tei:seriesStmt")


class Tei(_TeiBase):
    """xmlmap object for a TEI (Text Encoding Initiative) XML document"""

    id = fields.StringField("@xml:id")
    title = fields.StringField("tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title")
    author = fields.StringField(
        "tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:author/tei:name/tei:choice/tei:sic"
    )
    editor = fields.StringField(
        "tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:editor/tei:name/tei:choice/tei:sic"
    )

    header = fields.NodeField("tei:teiHeader", TeiHeader)
    front = fields.NodeField("tei:text/tei:front", TeiSection)
    body = fields.NodeField("tei:text/tei:body", TeiSection)
    back = fields.NodeField("tei:text/tei:back", TeiSection)
