#!/usr/bin/env python3
"""CLI entry point for RobustDocOCR package."""

import argparse
import sys
from robustdococr.preprocessing.pipeline import preprocess_document
from robustdococr.utils.image_utils import load_image

def main():
    """CLI entry point for RobustDocOCR."""
    parser = argparse.ArgumentParser(
        description="RobustDocOCR - Document OCR Preprocessing Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process single image
  robustdococr input.jpg --output output.jpg

  # Process with intermediate steps display
  robustdococr input.jpg --show-steps
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

    args = parser.parse_args()

    try:
        # Load image
        image = load_image(args.input)

        # Apply preprocessing pipeline
        results = preprocess_document(image, show_steps=args.show_steps)

        if args.output:
            import cv2
            cv2.imwrite(args.output, results['final'])
            print(f"Preprocessed image saved to: {args.output}")

        print("Processing completed successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()