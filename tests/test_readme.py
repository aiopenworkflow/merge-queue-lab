import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def readme_sentences():
    """Split README.md prose into sentences (inline code kept intact)."""
    text = (ROOT / "README.md").read_text()
    sentences = []
    for block in re.split(r"\n\s*\n", text):
        block = " ".join(block.split())
        if not block or block.startswith("#"):
            continue
        sentences.extend(s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z`])", block) if s)
    return sentences


class ReadmeOfflineTestCommandTests(unittest.TestCase):
    def test_one_sentence_names_python3_test_py_as_offline_test_command_run_from_repository_root(self):
        matches = [
            s
            for s in readme_sentences()
            if "`python3 test.py`" in s
            and "offline test" in s.lower()
            and "repository root" in s.lower()
        ]
        self.assertEqual(
            len(matches),
            1,
            "README must have exactly one sentence naming `python3 test.py` as the "
            "offline test command run from the repository root",
        )


if __name__ == "__main__":
    unittest.main()
