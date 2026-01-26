#!/usr/bin/env python3
"""Command-line interface for the Robust Document OCR Preprocessing Pipeline.

This module provides a CLI interface for processing document images and
comparing OCR results before and after preprocessing.
"""

import argparse
import os
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from preprocessing.pipeline import preprocess_document
from utils.image_utils import load_image, display_images
from utils.ocr_utils import compare_ocr

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Robust Document OCR Preprocessing Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process single image and show results
  python -m src.main input.jpg --show-steps

  # Process image and compare OCR results
  python -m src.main input.jpg --compare-ocr

  # Process image and save output
  python -m src.main input.jpg --output output.jpg
        """
    )

    parser.add_argument(
        "input",
        help="Input image file path",
        type=str
    )

    parser.add_argument(
        "--output",
        "-o",
        help="Output file path for preprocessed image",
        type=str,
        default=None
    )

    parser.add_argument(
        "--show-steps",
        action="store_true",
        help="Display intermediate processing steps"
    )

    parser.add_argument(
        "--compare-ocr",
        action="store_true",
        help="Compare OCR results before and after preprocessing"
    )

    parser.add_argument(
        "--no-display",
        action="store_true",
        help="Don't display any images (useful for batch processing)"
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output"
    )

    args = parser.parse_args()

    # Validate input file
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found")
        sys.exit(1)

    if args.verbose:
        print(f"Loading image: {args.input}")

    try:
        # Load and process image
        image = load_image(args.input)

        if args.verbose:
            print(f"Image loaded: {image.shape[1]}x{image.shape[0]} pixels")

        # Apply preprocessing pipeline
        results = preprocess_document(image, show_steps=args.show_steps and not args.no_display)

        if args.verbose:
            print(f"Preprocessing complete. Rotation applied: {results['rotation_angle']:.2f}°")

        # Save output if requested
        if args.output:
            if args.verbose:
                print(f"Saving preprocessed image to: {args.output}")
            cv2.imwrite(args.output, results['final'])
            if args.verbose:
                print("Image saved successfully")

        # Compare OCR if requested
        if args.compare_ocr:
            if args.verbose:
                print("Running OCR comparison...")
            compare_ocr(results['original'], results['final'], show_details=True)

        # Display final comparison if not disabled
        if not args.no_display and not args.show_steps:
            display_images(
                [results['original'], results['final']],
                ['Original Image', 'Preprocessed Image'],
                figsize=(12, 6)
            )

        if args.verbose:
            print("Processing complete!")

    except Exception as e:
        print(f"Error processing image: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()