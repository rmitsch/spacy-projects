""" Testing all project steps. """
import os

import pytest
from pathlib import Path
import sys
from spacy.cli.project.run import project_run


@pytest.mark.skipif(sys.platform == "win32", reason="Skipping on Windows (for now) due to platform-specific scripts.")
def test_nel_benchmark():
    exit(1)
