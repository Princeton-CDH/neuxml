# file test_xmlmap/test_cerp.py
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

import email
import unittest
import os

from neuxml.xmlmap import cerp
from neuxml.xmlmap.core import load_xmlobject_from_file


class TestCerp(unittest.TestCase):
    FIXTURE_FILE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "fixtures", "In.cerp"
    )

    def setUp(self):
        self.account = load_xmlobject_from_file(self.FIXTURE_FILE, cerp.Account)
        self.folder = self.account.folders[0]
        self.message = self.folder.messages[0]

    def testAccount(self):
        self.assertTrue(isinstance(self.account, cerp.Account))
        self.assertEqual(len(self.account.folders), 1)

    def testFolder(self):
        self.assertTrue(isinstance(self.folder, cerp.Folder))
        self.assertEqual(self.folder.name, "In")
        self.assertEqual(len(self.folder.messages), 1)

    def testMessage(self):
        self.assertTrue(isinstance(self.message, cerp.Message))
        self.assertEqual(self.message.local_id, 3)
        self.assertEqual(
            self.message.message_id, "<960XXXX01955_100560.XXXX_EHK76-1@CompuServe.COM>"
        )
        self.assertEqual(self.message.orig_date_list, ["1996-07-24T06:19:55-04:00"])
        self.assertEqual(self.message.from_list, ["Somebody <somebody@CompuServe.COM>"])
        self.assertEqual(self.message.to_list, ["Somebody Else <somebody@example.com>"])
        self.assertEqual(self.message.subject_list, ["various"])

        expect_header_names = [
            "Received",
            "Date",
            "From",
            "To",
            "Subject",
            "Message-Id",
            "Status",
        ]
        actual_header_names = [h.name for h in self.message.headers]
        self.assertEqual(actual_header_names, expect_header_names)

        self.assertEqual(self.message.eol, "LF")

    # simple email text fixture from RFC822 Appendix A
    simple_email_content = """This is a message just to say hello.
So, "Hello"."""

    simple_email = (
        """From: John Doe <jdoe@machine.example>
To: Mary Smith <mary@example.net>
Subject: Saying Hello
Date: Fri, 21 Nov 1997 09:55:06 -0600
Message-ID: <1234@local.machine.example>
Content-Type: text/plain; charset=us-ascii

%s"""
        % simple_email_content
    )

    def test_message_from_email(self):
        email_msg = email.message_from_string(self.simple_email)
        cerp_msg = cerp.Message.from_email_message(email_msg)

        self.assertEqual(email_msg["From"], cerp_msg.from_list[0])
        self.assertEqual(email_msg["To"], cerp_msg.to_list[0])
        # dates in different format, how to compare ?
        self.assertEqual(email_msg["Subject"], cerp_msg.subject_list[0])
        self.assertEqual(email_msg["Message-Id"], cerp_msg.message_id)
        self.assertEqual(self.simple_email_content, cerp_msg.body.content.content)

        # TODO: multiple recipients, attachments, etc.
