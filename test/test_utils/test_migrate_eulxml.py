from io import StringIO
import pathlib
import re
import sys
from unittest.mock import patch

from neuxml.utils.migrate_eulxml import is_valid, main


class TestMigrateEulxml:
    def test_is_valid(self):
        # hidden files/folders, site-packages should not be valid
        bad_path = pathlib.Path("/project/.git/example.py")
        assert not is_valid(bad_path)
        bad_path = pathlib.Path(
            "/project/venv/lib/python3.12/site-packages/pytest/__main__.py"
        )
        assert not is_valid(bad_path)
        good_path = pathlib.Path("/project/example.py")
        assert is_valid(good_path)

    def test_main(self):
        """integration tests for the migration script, which
        should hit every case and thus every helper function"""
        mock_args = ["/fake/path"]
        mock_file = "test/test_utils/fixtures/old_import.txt"
        with patch.object(pathlib.Path, "glob") as mock_glob:
            mock_glob.return_value = [pathlib.Path(mock_file)]
            with patch.object(pathlib.Path, "write_text") as mock_write_text:
                main(mock_args)
                output_text = mock_write_text.call_args[0][0]

                # should replace all eulxml with neuxml
                assert "eulxml" not in output_text
                assert "neuxml" in output_text

                # should replace `import xmlmap` with submodule imports
                assert "import xmlmap" not in output_text
                assert "from neuxml.xmlmap import core, fields" in output_text

                # should categorize imports correctly: core, fields, module
                assert re.search(
                    r"from neuxml\.xmlmap\.core import.*XmlObject", output_text
                )
                assert re.search(
                    r"from neuxml\.xmlmap\.fields import.*NodeField", output_text
                )
                assert "from neuxml.xmlmap import mods" in output_text

                # should replace inline references appropriately
                assert "xmlmap.StringField" not in output_text
                assert "fields.StringField" in output_text
                assert "xmlmap.XmlObject" not in output_text
                assert "core.XmlObject" in output_text
                assert "xmlmap.load_" not in output_text
                assert "core.load_" in output_text

                # should print exceptions with file path
                mock_write_text.side_effect = Exception("msg")
                with patch.object(sys, "stdout", new_callable=StringIO) as mock_stdout:
                    main(mock_args)
                    assert (
                        f"Failed to process {mock_file}: msg" in mock_stdout.getvalue()
                    )
