"""Deskewing module for document image straightening.

This module provides functions to detect and correct rotation in document images
using edge detection and Hough transform algorithms.
"""

import cv2
import numpy as np

def deskew_image(image):
    """Deskew/straighten document image using edge detection and Hough transform.

    Method:
    1. Detect edges using Canny edge detector
    2. Find lines using Hough Line Transform
    3. Calculate median rotation angle from detected lines
    4. Apply affine transformation to rotate image

    Technical approach:
    - Hough transform is robust to noise and partial line detection
    - Median angle prevents outliers from affecting rotation
    - Affine transformation preserves document structure

    Args:
        image (numpy.ndarray): Input document image (BGR or grayscale)

    Returns:
        tuple: (rotated_image, rotation_angle) where rotated_image is the deskewed image
               and rotation_angle is the angle applied in degrees

    Raises:
        ValueError: If image cannot be processed
    """
    # Convert to grayscale
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()

    # Edge detection with Canny
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Detect lines using Hough Transform
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

    # Calculate rotation angles from detected lines
    angles = []
    if lines is not None:
        for rho, theta in lines[:, 0]:
            angle = np.degrees(theta) - 90
            # Filter extreme angles
            if -45 < angle < 45:
                angles.append(angle)

    # No lines detected - return original
    if len(angles) == 0:
        return image, 0

    # Get median angle (robust to outliers)
    median_angle = np.median(angles)

    # Only rotate if angle is significant (> 0.5 degrees)
    if abs(median_angle) < 0.5:
        return image, 0

    # Perform rotation using affine transformation
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, median_angle, 1.0)

    # Rotate with interpolation to preserve quality
    rotated = cv2.warpAffine(
        image,
        rotation_matrix,
        (w, h),
        flags=cv2.INTER_CUBIC,  # High-quality interpolation
        borderMode=cv2.BORDER_REPLICATE
    )

    return rotated, median_angle