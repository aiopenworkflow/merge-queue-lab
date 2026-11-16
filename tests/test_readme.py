import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sentences(text):
    """Split prose into sentences on terminal punctuation followed by whitespace."""
    flat = " ".join(text.split())
    return [s for s in re.split(r"(?<=[.!?])\s+", flat) if s]


class ReadmeOfflineTestInstructionsTests(unittest.TestCase):
    def test_readme_has_one_sentence_naming_offline_test_command_from_repository_root(self):
        readme = (ROOT / "README.md").read_text()
        matching = [
            s
            for s in sentences(readme)
            if "`python3 test.py`" in s
            and "offline" in s.lower()
            and "repository root" in s.lower()
        ]
        self.assertEqual(
            len(matching),
            1,
            "README must contain exactly one sentence naming `python3 test.py` "
            "as the offline test command run from the repository root",
        )

    def test_documented_command_matches_ci(self):
        ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text()
        self.assertIn("run: python3 test.py", ci)


if __name__ == "__main__":
    unittest.main()
