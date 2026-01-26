"""Test suite for the Robust Document OCR Preprocessing Pipeline.

This package contains unit tests for all components of the preprocessing pipeline.
"""

import os
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))