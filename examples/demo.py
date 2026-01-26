#!/usr/bin/env python3
"""Demo script for the Robust Document OCR Preprocessing Pipeline.

This script demonstrates how to use the preprocessing pipeline with sample images.
"""

import os
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from preprocessing.pipeline import preprocess_document, DocumentPreprocessor
from utils.image_utils import load_image, display_images
from utils.ocr_utils import compare_ocr

def main():
    """Run the demo with sample images."""
    print("Robust Document OCR Preprocessing Pipeline Demo")
    print("=" * 60)

    # Check if we have sample images
    sample_dir = Path(__file__).parent / "sample_images"

    if not sample_dir.exists():
        print("No sample images found. Creating sample image...")
        sample_dir.mkdir(exist_ok=True)

        # Create a simple test image
        import cv2
        import numpy as np

        # Create white background
        img = np.ones((300, 400, 3), dtype=np.uint8) * 255

        # Add some text-like patterns
        cv2.putText(img, "SAMPLE DOCUMENT", (50, 50),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        cv2.putText(img, "ID: 123456789", (50, 100),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)
        cv2.putText(img, "NAME: JOHN DOE", (50, 150),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)
        cv2.putText(img, "DATE: 2026-01-26", (50, 200),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)

        # Add some noise and rotation to simulate real document
        # Rotate slightly
        (h, w) = img.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, -5, 1.0)
        img = cv2.warpAffine(img, M, (w, h))

        # Add some noise
        noise = np.random.normal(0, 10, img.shape).astype(np.uint8)
        img = cv2.add(img, noise)

        # Save the sample image
        sample_path = sample_dir / "sample_document.jpg"
        cv2.imwrite(str(sample_path), img)
        print(f"Created sample image: {sample_path}")

        image_paths = [sample_path]
    else:
        # Get available sample images
        image_paths = list(sample_dir.glob("*.*"))
        if not image_paths:
            print("No sample images found in sample_images directory")
            return

    print(f"Found {len(image_paths)} sample image(s)")

    # Process each image
    for i, image_path in enumerate(image_paths, 1):
        print(f"\nProcessing image {i}/{len(image_paths)}: {image_path.name}")

        try:
            # Load image
            img = load_image(str(image_path))
            print(f"  Image size: {img.shape[1]}x{img.shape[0]} pixels")

            # Method 1: Using function directly
            print("\n  Method 1: Using preprocess_document() function")
            results = preprocess_document(img, show_steps=False)

            # Method 2: Using class
            print("\n  Method 2: Using DocumentPreprocessor class")
            preprocessor = DocumentPreprocessor()
            class_results = preprocessor.preprocess(img, show_steps=False)

            # Show final comparison
            print("\n  Final Results:")
            display_images(
                [results['original'], results['final']],
                ['Original', 'Preprocessed'],
                figsize=(12, 6)
            )

            # Compare OCR (if Tesseract is available)
            try:
                print("\n  OCR Comparison:")
                compare_ocr(results['original'], results['final'], show_details=True)
            except Exception as e:
                print(f"  OCR comparison failed: {str(e)}")
                print("  (Tesseract may not be installed or configured)")

        except Exception as e:
            print(f"  Error processing image: {str(e)}")

    print("\nDemo completed!")

if __name__ == "__main__":
    main()