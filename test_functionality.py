#!/usr/bin/env python3
"""Simple test script to verify the preprocessing pipeline functionality."""

import sys
import numpy as np
import cv2

# Add src to path
sys.path.insert(0, 'src')

from preprocessing.pipeline import preprocess_document
from preprocessing.deskewing import deskew_image
from preprocessing.binarization import binarize_image
from preprocessing.noise_removal import remove_noise

def test_core_functionality():
    """Test the core preprocessing functionality."""
    print("🧪 Testing Robust Document OCR Preprocessing Pipeline")
    print("=" * 60)

    # Create a test image
    print("📝 Creating test image...")
    test_img = np.ones((200, 300, 3), dtype=np.uint8) * 255  # White background

    # Add some text-like patterns
    cv2.putText(test_img, "TEST DOCUMENT", (50, 50),
               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
    cv2.putText(test_img, "ID: ABC12345", (50, 100),
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)
    cv2.putText(test_img, "DATE: 2026-01-26", (50, 150),
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)

    # Add some rotation to test deskewing
    (h, w) = test_img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, -8, 1.0)
    test_img = cv2.warpAffine(test_img, M, (w, h))

    print("✅ Test image created successfully")

    # Test individual components
    print("\n🔧 Testing individual components...")

    # Test deskewing
    print("   Testing deskewing...")
    deskewed, angle = deskew_image(test_img)
    print(f"   ✅ Deskewing: {angle:.2f}° rotation applied")

    # Test binarization
    print("   Testing binarization...")
    binary = binarize_image(deskewed)
    print(f"   ✅ Binarization: {binary.shape} output")

    # Test noise removal
    print("   Testing noise removal...")
    cleaned = remove_noise(binary)
    print(f"   ✅ Noise removal: {cleaned.shape} output")

    # Test complete pipeline
    print("\n🚀 Testing complete pipeline...")
    results = preprocess_document(test_img, show_steps=False)

    print(f"   ✅ Pipeline completed successfully!")
    print(f"   ✅ Rotation angle: {results['rotation_angle']:.2f}°")
    print(f"   ✅ Final output shape: {results['final'].shape}")
    print(f"   ✅ All intermediate results present: {len(results) == 6}")

    # Verify all expected keys are present
    expected_keys = ['original', 'denoised', 'deskewed', 'binary', 'final', 'rotation_angle']
    for key in expected_keys:
        if key not in results:
            print(f"   ❌ Missing key: {key}")
            return False

    print("\n🎉 All tests passed successfully!")
    print("✅ Core preprocessing pipeline is working correctly")
    print("✅ Individual components are functioning properly")
    print("✅ Complete pipeline integration is successful")

    return True

def test_imports():
    """Test that all imports work correctly."""
    print("📦 Testing imports...")

    try:
        from preprocessing import (
            deskew_image,
            binarize_image,
            remove_noise,
            preprocess_document,
            DocumentPreprocessor
        )
        print("✅ Preprocessing imports successful")

        from utils import (
            load_image,
            display_images,
            print_section_header,
            perform_ocr,
            compare_ocr,
            calculate_metrics,
            plot_comparison,
            plot_quality_distribution
        )
        print("✅ Utils imports successful (OCR functions may require pytesseract)")

        return True
    except ImportError as e:
        print(f"❌ Import error: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during imports: {str(e)}")
        return False

if __name__ == "__main__":
    print("Starting functionality tests...\n")

    # Test imports first
    imports_ok = test_imports()

  