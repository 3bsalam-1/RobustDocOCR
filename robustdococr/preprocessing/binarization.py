"""Binarization module for document image thresholding.

This module provides adaptive thresholding functions specifically designed for
mobile-captured documents with uneven lighting conditions.
"""

import cv2
import numpy as np

def binarize_image(image):
    """Binarize image using Adaptive Gaussian Thresholding.

    Technical comparison: Adaptive Thresholding vs Otsu's Method

    1. ADAPTIVE THRESHOLDING (Chosen):
       - Handles varying lighting conditions (shadows, glare)
       - Works well with uneven illumination across document
       - Computes threshold locally for each pixel region
       - Perfect for mobile-captured documents (MIDV-500)

    2. OTSU'S THRESHOLDING (Not chosen):
       - Assumes uniform lighting across entire image
       - Fails with shadows or gradient illumination
       - Single global threshold for whole image

    Parameters:
    - blockSize=25: Large neighborhood for stable local threshold
    - C=10: Gentle adjustment (prevents over-aggressive thresholding)
    - Gaussian weighting: Smoother transitions than mean

    Args:
        image (numpy.ndarray): Input document image (BGR or grayscale)

    Returns:
        numpy.ndarray: Binary image (black and white)

    Raises:
        ValueError: If image cannot be processed
    """
    # Convert to grayscale
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()

    # CRITICAL: Apply CLAHE before binarization
    # This enhances local contrast and helps adaptive thresholding
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    # Apply Adaptive Gaussian Thresholding
    binary = cv2.adaptiveThreshold(
        enhanced,                           # Input image
        255,                                # Max value
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,     # Gaussian-weighted mean
        cv2.THRESH_BINARY,                  # Binary output
        blockSize=25,                       # Large block = gentler thresholding
        C=10                                # Constant subtracted (gentle)
    )

    return binary