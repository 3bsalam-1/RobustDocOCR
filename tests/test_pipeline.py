"""Unit tests for the complete preprocessing pipeline."""

import pytest
import numpy as np
import cv2
from preprocessing.pipeline import preprocess_document, DocumentPreprocessor

def test_preprocess_document_basic():
    """Test basic pipeline functionality."""
    # Create a simple test image
    image = np.ones((100, 100, 3), dtype=np.uint8) * 255
    cv2.rectangle(image, (20, 20), (80, 80), (0, 0, 0), -1)

    results = preprocess_document(image, show_steps=False)

    # Check that all expected keys are present
    expected_keys = ['original', 'denoised', 'deskewed', 'binary', 'final', 'rotation_angle']
    for key in expected_keys:
        assert key in results

    # Check types
    assert isinstance(results['original'], np.ndarray)
    assert isinstance(results['denoised'], np.ndarray)
    assert isinstance(results['deskewed'], np.ndarray)
    assert isinstance(results['binary'], np.ndarray)
    assert isinstance(results['final'], np.ndarray)
    assert isinstance(results['rotation_angle'], (int, float, np.number))

def test_document_preprocessor_class():
    """Test the DocumentPreprocessor class."""
    # Create test image
    image = np.ones((100, 100, 3), dtype=np.uint8) * 255

    # Test class instantiation and usage
    preprocessor = DocumentPreprocessor()
    results = preprocessor.preprocess(image, show_steps=False)

    # Check that results are returned
    assert isinstance(results, dict)
    assert 'final' in results

def test_pipeline_preserves_image_shape():
    """Test that pipeline preserves original image dimensions."""
    image = np.ones((100, 150, 3), dtype=np.uint8) * 255

    results = preprocess_document(image, show_steps=False)

    # All images should have same height and width as original
    assert results['original'].shape[:2] == (100, 150)
    assert results['denoised'].shape[:2] == (100, 150)
    assert results['deskewed'].shape[:2] == (100, 150)
    assert results['binary'].shape[:2] == (100, 150)
    assert results['final'].shape[:2] == (100, 150)

def test_pipeline_with_grayscale_input():
    """Test pipeline with grayscale input image."""
    image = np.ones((100, 100), dtype=np.uint8) * 255

    results = preprocess_document(image, show_steps=False)

    assert isinstance(results, dict)
    assert 'final' in results
    assert results['final'].shape == (100, 100)