"""Utility modules for the OCR preprocessing pipeline.

This package provides utility functions for image processing, OCR operations,
and visualization tasks.
"""

from .image_utils import load_image, display_images, print_section_header
from .ocr_utils import perform_ocr, compare_ocr, calculate_metrics
from .visualization import plot_comparison, plot_quality_distribution

__all__ = [
    "load_image",
    "display_images",
    "print_section_header",
    "perform_ocr",
    "compare_ocr",
    "calculate_metrics",
    "plot_comparison",
    "plot_quality_distribution",
]

# Package version
__version__ = "1.0.2"
__author__ = "Ahmed Mohamed"
__license__ = "MIT"
__email__ = "3bsalam0@gmail.com"
