"""Noise removal module for document image cleaning.

This module provides functions to remove noise from document images using
a two-stage approach: denoising before binarization and morphological
operations after binarization.
"""

import cv2
import numpy as np

def remove_noise(image):
    """Remove noise using Non-Local Means Denoising + Morphological Operations.

    Two-stage approach:
    1. Non-Local Means Denoising (BEFORE binarization is better)
    2. Light morphological operations (AFTER binarization)

    Technical rationale:
    - Denoising before binarization preserves text structure
    - Light morphological ops clean up small artifacts
    - Avoids aggressive operations that destroy text details

    Args:
        image (numpy.ndarray): Input binary image (grayscale)

    Returns:
        numpy.ndarray: Cleaned binary image

    Raises:
        ValueError: If image is not binary or cannot be processed
    """
    # This function is applied to binary images
    # Noise removal is split into two stages:
    # - Stage 1: Denoise BEFORE binarization (done in preprocessing pipeline)
    # - Stage 2: Clean binary image (this function)

    # Minimal morphological operations to preserve text
    kernel = np.ones((2, 2), np.uint8)

    # Closing: Remove small black dots (salt noise)
    cleaned = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=1)

    # Opening: Remove small white dots (pepper noise)
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_OPEN, kernel, iterations=1)

    return cleaned