"""OCR utility functions for document text extraction and comparison.

This module provides functions for performing OCR on document images and
comparing results before and after preprocessing.
"""

import cv2
import pytesseract

def perform_ocr(image):
    """Perform OCR using Tesseract with optimized configuration.

    PSM (Page Segmentation Mode) 6:
    - Assumes uniform block of text
    - Best for document pages

    Args:
        image (numpy.ndarray): Input document image

    Returns:
        str: Extracted text from OCR

    Raises:
        RuntimeError: If Tesseract is not properly installed
    """
    if len(image.shape) == 3:
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        rgb = image

    # Optimized Tesseract config
    config = '--oem 3 --psm 6'  # LSTM engine, uniform text block
    text = pytesseract.image_to_string(rgb, lang='eng', config=config)

    return text

def calculate_metrics(text_before, text_after):
    """Calculate OCR quality metrics.

    Args:
        text_before (str): OCR text before preprocessing
        text_after (str): OCR text after preprocessing

    Returns:
        dict: Dictionary containing metrics:
              - 'chars_before': Character count before
              - 'chars_after': Character count after
              - 'change': Difference in character count
              - 'retention': Retention rate percentage
    """
    chars_before = len(text_before.strip())
    chars_after = len(text_after.strip())
    change = chars_after - chars_before
    retention = (chars_after / chars_before * 100) if chars_before > 0 else 0

    return {
        'chars_before': chars_before,
        'chars_after': chars_after,
        'change': change,
        'retention': retention
    }

def compare_ocr(original_image, preprocessed_image, show_details=True):
    """Compare OCR results before and after preprocessing.

    Args:
        original_image (numpy.ndarray): Original document image
        preprocessed_image (numpy.ndarray): Preprocessed document image
        show_details (bool): Whether to print detailed comparison

    Returns:
        dict: Dictionary containing:
              - 'text_before': OCR text from original
              - 'text_after': OCR text from preprocessed
              - 'metrics': Quality metrics
    """
    # Run OCR on both
    text_before = perform_ocr(original_image)
    text_after = perform_ocr(preprocessed_image)

    # Calculate metrics
    metrics = calculate_metrics(text_before, text_after)

    if show_details:
        print_section_header("OCR COMPARISON RESULTS")

        print("\nBEFORE PREPROCESSING:")
        print("-" * 70)
        preview_before = text_before[:400] if len(text_before) > 400 else text_before
        print(preview_before)
        if len(text_before) > 400:
            print("... (truncated)")
        print(f"\nTotal characters detected: {metrics['chars_before']}")

        print("\nAFTER PREPROCESSING:")
        print("-" * 70)
        preview_after = text_after[:400] if len(text_after) > 400 else text_after
        print(preview_after)
        if len(text_after) > 400:
            print("... (truncated)")
        print(f"\nTotal characters detected: {metrics['chars_after']}")

        print("\nMETRICS:")
        print("-" * 70)
        print(f"   Character Change: {metrics['change']:+d}")
        print(f"   Retention Rate: {metrics['retention']:.1f}%")

        # Quality assessment
        if metrics['retention'] >= 95:
            print(f"   Quality: EXCELLENT (minimal text loss)")
        elif metrics['retention'] >= 85:
            print(f"   Quality: GOOD (acceptable retention)")
        elif metrics['retention'] >= 70:
            print(f"   Quality: FAIR (some text loss)")
        else:
            print(f"   Quality: POOR (significant text loss)")

        print("="*70)

    return {
        'text_before': text_before,
        'text_after': text_after,
        'metrics': metrics
    }

def print_section_header(title):
    """Print formatted section header (internal utility).

    Args:
        title (str): Section title to print
    """
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)