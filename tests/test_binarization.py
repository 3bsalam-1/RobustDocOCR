"""Unit tests for the binarization module."""

import pytest
import numpy as np
import cv2
from preprocessing.binarization import binarize_image

def test_binarize_image_basic():
    """Test basic binarization functionality."""
    # Create a simple test image
    image = np.ones((100, 100, 3), dtype=np.uint8) * 255
    cv2.rectangle(image, (20, 20), (80, 80), (0, 0, 0), -1)

    result = binarize_image(image)

    assert isinstance(result, np.ndarray)
    assert len(result.shape) == 2  # Should be grayscale
    assert result.dtype == np.uint8

def test_binarize_image_grayscale():
    """Test binarization with grayscale input."""
    # Create grayscale test image
    image = np.ones((100, 100), dtype=np.uint8) * 255
    cv2.rectangle(image, (20, 20), (80, 80), 0, -1)

    result = binarize_image(image)

    assert isinstance(result, np.ndarray)
    assert len(result.shape) == 2
    assert result.dtype == np.uint8

def test_binarize_image_output_range():
    """Test that binarization output is properly binary (0 or 255)."""
    image = np.ones((50, 50, 3), dtype=np.uint8) * 128  # Gray image

    result = binarize_image(image)

    # Check that all values are either 0 or 255
    unique_values = np.unique(result)
    assert np.all(np.isin(unique_values, [0, 255]))