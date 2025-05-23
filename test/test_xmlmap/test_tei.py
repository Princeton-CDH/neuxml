# file test_xmlmap/test_tei.py
#
#   Copyright 2025 Center for Digital Humanities, Princeton University
#   Copyright 2011 Emory University Libraries (eulxml)
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

#!/usr/bin/env python

import unittest
from os import path

from neuxml.xmlmap import teimap
from neuxml.xmlmap.core import load_xmlobject_from_file
from neuxml.xmlmap.fields import NodeListField


class ExtendedTei(teimap.Tei):
    # additional mappings for testing
    figure = NodeListField("//tei:figure", teimap.TeiFigure)
    interpGroup = NodeListField("//tei:interpGrp", teimap.TeiInterpGroup)


class TestTei(unittest.TestCase):
    FIXTURE_FILE = path.join(
        path.dirname(path.abspath(__file__)), "fixtures", "tei_clarke.xml"
    )

    def setUp(self):
        self.tei = load_xmlobject_from_file(self.FIXTURE_FILE, ExtendedTei)

    def testInit(self):
        self.assertTrue(isinstance(self.tei, teimap.Tei))

    def testBasicFields(self):
        self.assertEqual(self.tei.id, "clarke")
        self.assertEqual(self.tei.title, "A Treasury of War Poetry: Electronic Edition")
        # self.assertEqual(self.tei.author, "Various")
        self.assertEqual(self.tei.editor, "George Herbert Clarke")

        self.assertTrue(isinstance(self.tei.front, teimap.TeiSection))
        self.assertTrue(isinstance(self.tei.body, teimap.TeiSection))
        self.assertTrue(isinstance(self.tei.back, teimap.TeiSection))
        self.assertTrue(isinstance(self.tei.header, teimap.TeiHeader))

        self.assertTrue(isinstance(self.tei.body.div[0], teimap.TeiDiv))

    def test_teiHeader(self):
        header = self.tei.header
        self.assertEqual("A Treasury of War Poetry: Electronic Edition", header.title)
        self.assertTrue(isinstance(header.editor_list[0], teimap.TeiName))
        self.assertEqual("Clarke, George Herbert", header.editor_list[0].reg)
        self.assertEqual("George Herbert Clarke", header.editor_list[0].value)
        self.assertTrue(
            "Lewis H. Beck Center for Electronic Collections" in header.publisher
        )
        self.assertEqual("2004", header.publication_date)
        self.assertTrue(
            "download, transmit, or otherwise reproduce," in header.availability
        )
        self.assertTrue(
            "A Treasury of War Poetry: British" in header.source_description
        )
        self.assertTrue("The Great War" in header.series_statement)

    def testTeiDiv(self):
        div = self.tei.body.div[0]
        self.assertEqual("clarke005", div.id)
        self.assertEqual("Chapter", div.type)
        self.assertEqual("America", div.title)
        # subdiv (recursive mapping)
        self.assertTrue(isinstance(div.div[0], teimap.TeiDiv))
        self.assertEqual("clarke006", div.div[0].id)
        self.assertEqual("The Choice", div.div[0].title)
        self.assertEqual("Rudyard Kipling", div.div[0].author)

        self.assertTrue(
            "THE RIVERSIDE PRESS LIMITED, EDINBURGH" in self.tei.back.div[1].text
        )

    def testTeiFigure(self):
        self.assertTrue(isinstance(self.tei.figure[0], teimap.TeiFigure))
        self.assertEqual("chateau_thierry2", self.tei.figure[0].entity)
        self.assertEqual("Chateau-Thierry", self.tei.figure[0].head)
        self.assertEqual("nat-fr mil-f con-r im-ph t-wwi", self.tei.figure[0].ana)
        self.assertTrue("photo of ruined houses" in self.tei.figure[0].description)

    def testTeiInterpGroup(self):
        self.assertTrue(isinstance(self.tei.interpGroup[0], teimap.TeiInterpGroup))
        self.assertTrue(isinstance(self.tei.interpGroup[0].interp[0], teimap.TeiInterp))
        self.assertEqual("image", self.tei.interpGroup[0].type)
        self.assertEqual("time period", self.tei.interpGroup[1].type)
        self.assertEqual("im-ph", self.tei.interpGroup[0].interp[0].id)
        self.assertEqual("photo", self.tei.interpGroup[0].interp[0].value)
        self.assertEqual("mil-na", self.tei.interpGroup[2].interp[1].id)

    def testTeiLineGroup(self):
        poem = self.tei.body.div[0].div[2]  # using clarke008
        self.assertTrue(isinstance(poem.linegroup[0], teimap.TeiLineGroup))
        self.assertTrue(isinstance(poem.linegroup[0].line[0], teimap.TeiLine))
        self.assertEqual(4, poem.linegroup[1].line[3].indent())
        self.assertEqual(0, poem.linegroup[0].line[2].indent())

    # print poem.linegroup[0].line[2].indent()

    def testTeiEpigraph(self):
        epigraph = self.tei.front.div[1].epigraph[0]  # using clarke002
        self.assertEqual("epigraph", self.tei.front.div[1].type)
        self.assertTrue(isinstance(epigraph, teimap.TeiEpigraph))
        self.assertTrue(isinstance(epigraph.quote[0], teimap.TeiQuote))
        self.assertTrue(isinstance(epigraph.quote[0].line[0], teimap.TeiLine))
