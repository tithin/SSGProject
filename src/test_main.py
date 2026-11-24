import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "index.html"

class TestMain(unittest.TestCase): 
    def test_import_does_not_rebuild_docs(self):
        before = os.stat(INDEX).st_mtime_ns

        sys.modules.pop("main", None)
        import main
        after = os.stat(INDEX).st_mtime_ns
        self.assertEqual(before, after)

