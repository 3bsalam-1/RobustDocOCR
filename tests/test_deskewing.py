"""Unit tests for the deskewing module."""

import pytest
import numpy as np
import cv2
from preprocessing.deskewing import deskew_image

def test_deskew_image_basic():
    """Test basic deskewing functionality."""
    # Create a simple test image (white background with black rectangle)
    image = np.ones((100, 100, 3), dtype=np.uint8) * 255
    cv2.rectangle(image, (20, 20), (80, 80), (0, 0, 0), -1)

    # Test that deskewing doesn't crash and returns expected types
    result, angle = deskew_image(image)

    assert isinstance(result, np.ndarray)
    assert isinstance(angle, (int, float, np.number))
    assert result.shape == image.shape

def test_deskew_image_grayscale():
    """Test deskewing with grayscale image."""
    # Create grayscale test image
    image = np.ones((100, 100), dtype=np.uint8) * 255
    cv2.rectangle(image, (20, 20), (80, 80), 0, -1)

    result, angle = deskew_image(image)

    assert isinstance(result, np.ndarray)
    assert isinstance(angle, (int, float, np.number))
    assert result.shape == image.shape

def test_deskew_image_no_lines():
    """Test deskewing when no lines are detected."""
    # Create a blank image (should return original with 0 angle)
    image = np.ones((100, 100, 3), dtype=np.uint8) * 255

    result, angle = deskew_image(image)

    assert np.array_equal(result, image)
    assert angle == 0

def test_deskew_image_small_angle():
    """Test that small angles (< 0.5°) are not corrected."""
    # This is harder to test without actual rotation, but we can verify
    # the function handles edge cases properly
    image = np.ones((100, 100, 3), dtype=np.uint8) * 255

    # Add some edges that might result in small angle detection
    cv2.line(image, (10, 10), (90, 10), (0, 0, 0), 1)

    result, angle = deskew_image(image)

    assert isinstance(result, np.ndarray)
    assert isinstance(angle, (int, float, np.number))