"""RobustDocOCR - A robust preprocessing pipeline for document OCR."""

__version__ = "1.0.3"
__author__ = "Ahmed Mohamed"
__email__ = "3bsalam0@gmail.com"

# Import main modules for easy access
from .preprocessing.pipeline import preprocess_document
from .utils.image_utils import load_image
from .utils.ocr_utils import perform_ocr

__all__ = [
    "preprocess_document",
    "load_image", 
    "perform_ocr",
    "__version__",
    "__author__",
    "__email__"
]
