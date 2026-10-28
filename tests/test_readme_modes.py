import ast
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def accepted_modes():
    """Return the mode strings test.py accepts, read from its `in {...}` check."""
    tree = ast.parse((ROOT / "test.py").read_text())
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Compare)
            and len(node.ops) == 1
            and isinstance(node.ops[0], ast.In)
            and isinstance(node.comparators[0], ast.Set)
        ):
            values = {
                elt.value
                for elt in node.comparators[0].elts
                if isinstance(elt, ast.Constant) and isinstance(elt.value, str)
            }
            if values:
                return values
    raise AssertionError("test.py has no accepted-mode set")


class ReadmeModesTests(unittest.TestCase):
    def modes_section(self):
        readme = (ROOT / "README.md").read_text()
        match = re.search(r"^## Modes[ \t]*\n(.*?)(?=^## |\Z)", readme, re.M | re.S)
        self.assertIsNotNone(match, "README must contain a Modes section")
        return match.group(1)

    def test_modes_section_names_every_mode_test_py_accepts(self):
        section = self.modes_section()
        modes = accepted_modes()
        self.assertEqual(modes, {"v1", "v2"})
        for mode in sorted(modes):
            self.assertRegex(section, r"\b%s\b" % re.escape(mode))

    def test_modes_section_describes_enabled_feature_compatibility_rule(self):
        section = self.modes_section().lower()
        self.assertIn("rejects", section)
        self.assertIn("enabled feature", section)
        self.assertIn("lacks support", section)
        self.assertIn("active mode", section)
        self.assertIn("test.py", section)


if __name__ == "__main__":
    unittest.main()
