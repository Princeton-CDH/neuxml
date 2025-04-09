import argparse
import pathlib
import re

"""Command line script for migrating python package from eulxml to neuxml."""

# match definitions from the xmlmap.fields submodule; the rest are from core
fields_submodule_re = r"Field|Mapper|NodeList"


def repl_fields_or_core(match):
    """replace inline xmlmap.XXX with fields.XXX or core.XXX"""
    definition = match.groups()[0]
    if re.search(fields_submodule_re, definition):
        return f"fields.{definition}"
    else:
        return f"core.{definition}"


# submodules themselves can be imported directly from xmlmap
submodule_names = ["core", "cerp", "dc", "fields", "eadmap", "mods", "premis", "teimap"]


def get_imports(items):
    """pull out individual definitions from imports"""
    items = [item.strip().split()[0] for item in items if item.strip()]
    # submodule imports
    submodules = [i for i in items if i in submodule_names]
    # separate into fields and core imports
    fields = [i for i in items if re.search(fields_submodule_re, i)]
    core = [i for i in items if i not in [*fields, *submodules]]
    return fields, core, submodules


def replace_imports(fields, core, submodules):
    """replace import statements to use submodules where necessary"""
    imports = []
    if fields:
        imports.append(f"from neuxml.xmlmap.fields import {', '.join(fields)}")
    if core:
        imports.append(f"from neuxml.xmlmap.core import {', '.join(core)}")
    if submodules:
        imports.append(f"from neuxml.xmlmap import {', '.join(submodules)}")
    return "\n".join(imports)


def fix_xmlmap(code):
    """helper function to migrate xmlmap imports to direct references"""

    # handle `from neuxml import xmlmap`
    match = re.search("from neuxml import xmlmap", code)
    if match:
        # add imports for core and fields directly
        code = re.sub(
            "from neuxml import xmlmap", "from neuxml.xmlmap import core, fields", code
        )
        # update inline references to point to fields.XXX or core.XXX
        code = re.sub(
            r"(?<!from\s)(?<!import\s)(?<!\.)\bxmlmap\.(\w+)", repl_fields_or_core, code
        )

    # handle `from neuxml.xmlmap import (\n Field, XmlObject, ...\n)`
    multiline_pattern = re.compile(r"from neuxml\.xmlmap import \((.*?)\)", re.DOTALL)
    code = multiline_pattern.sub(
        lambda m: replace_imports(*get_imports(m.group(1).split(","))), code
    )

    # handle `from neuxml.xmlmap import Field, XmlObject, ...`
    singleline_pattern = re.compile(r"from neuxml\.xmlmap import ([^\n]+)")
    code = singleline_pattern.sub(
        lambda m: replace_imports(*get_imports(m.group(1).split(","))), code
    )

    # handle `from neuxml.xmlmap import *`
    code = re.sub(
        r"from neuxml\.xmlmap import \*",
        "from neuxml.xmlmap.fields import *\nfrom neuxml.xmlmap.core import *",
        code,
    )

    return code


def is_valid(path):
    """consider hidden files/folders and venv site-packages invalid for migration"""
    return not any(
        (part for part in path.parts if part.startswith(".") or "site-packages" in part)
    )


def main(arg_list=None):
    """Handle command line arguments and run migration functions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "project_path",
        type=pathlib.Path,
        help="The path to the root of a project using eulxml",
    )

    args = parser.parse_args(arg_list)

    # migrate every valid python file in project path and subdirectories
    for filepath in args.project_path.glob("**/*.py"):
        if is_valid(filepath):
            try:
                code = filepath.read_text(encoding="utf-8")
                migrated_code = fix_xmlmap(re.sub("eulxml", "neuxml", code))
                filepath.write_text(migrated_code, encoding="utf-8")
            except Exception as e:
                print(f"Failed to process {filepath}: {e}")


if __name__ == "__main__":
    main()
