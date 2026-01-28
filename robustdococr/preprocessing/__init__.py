"""Robust Document OCR Preprocessing Pipeline

This package provides a complete preprocessing pipeline for document OCR,
specifically designed for mobile-captured ID documents.
"""

from .deskewing import deskew_image
from .binarization import binarize_image
from .noise_removal import remove_noise
from .pipeline import preprocess_document, DocumentPreprocessor

__all__ = [
    "deskew_image",
    "binarize_image",
    "remove_noise",
    "preprocess_document",
    "DocumentPreprocessor",
]

# Package version
__version__ = "1.0.3"
__author__ = "Ahmed Mohamed"
__license__ = "MIT"
__email__ = "3bsalam0@gmail.com"
