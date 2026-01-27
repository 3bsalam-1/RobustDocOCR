"""Main preprocessing pipeline module.

This module provides the complete document preprocessing pipeline that combines
all individual processing stages into a cohesive workflow.
"""

import cv2
from .deskewing import deskew_image
from .binarization import binarize_image
from .noise_removal import remove_noise

class DocumentPreprocessor:
    """Document preprocessing pipeline class.

    This class provides a complete preprocessing pipeline for document OCR,
    combining deskewing, binarization, and noise removal stages.
    """

    def __init__(self):
        """Initialize the document preprocessor."""
        pass

    def preprocess(self, image, show_steps=False):
        """Apply complete preprocessing pipeline to document image.

        Pipeline:
        1. Deskewing → Straighten rotated documents
        2. Binarization → Convert to black & white with adaptive thresholding
        3. Noise Removal → Clean up artifacts

        Args:
            image (numpy.ndarray): Input document image
            show_steps (bool): Whether to display intermediate results

        Returns:
            dict: Dictionary with all intermediate results including:
                  - 'original': Original image
                  - 'denoised': Denoised grayscale image
                  - 'deskewed': Deskewed image
                  - 'binary': Binarized image
                  - 'final': Final preprocessed image
                  - 'rotation_angle': Rotation angle applied
        """
        return preprocess_document(image, show_steps)

def preprocess_document(image, show_steps=False):
    """Complete 3-stage preprocessing pipeline for document OCR.

    Pipeline:
    1. Deskewing → Straighten rotated documents
    2. Binarization → Convert to black & white with adaptive thresholding
    3. Noise Removal → Clean up artifacts

    Args:
        image (numpy.ndarray): Input document image
        show_steps (bool): Whether to display intermediate results

    Returns:
        dict: Dictionary with all intermediate results
    """
    # Stage 0: Denoise BEFORE everything (on color/grayscale)
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()

    # Non-local means denoising on grayscale
    denoised_gray = cv2.fastNlMeansDenoising(gray, h=10)

    # Convert back to BGR for deskewing (if needed)
    if len(image.shape) == 3:
        denoised_bgr = cv2.cvtColor(denoised_gray, cv2.COLOR_GRAY2BGR)
    else:
        denoised_bgr = denoised_gray

    # STAGE 1: Deskewing
    deskewed, rotation_angle = deskew_image(denoised_bgr)

    # STAGE 2: Binarization (includes CLAHE enhancement)
    binary = binarize_image(deskewed)

    # STAGE 3: Noise Removal
    final = remove_noise(binary)

    results = {
        'original': image,
        'denoised': denoised_bgr,
        'deskewed': deskewed,
        'binary': binary,
        'final': final,
        'rotation_angle': rotation_angle
    }

    if show_steps:
        _display_images(
            [results['original'], results['denoised'], results['deskewed'],
             results['binary'], results['final']],
            ['1. Original', '2. Denoised', f'3. Deskewed\n({rotation_angle:.2f}°)',
             '4. Binarized', '5. Final'],
            figsize=(24, 5)
        )

    return results

def _display_images(images, titles, figsize=(20, 8), cmap='gray'):
    """Display multiple images in a row with titles (internal utility).

    Args:
        images (list): List of images to display
        titles (list): List of titles for each image
        figsize (tuple): Figure size
        cmap (str): Colormap for grayscale images
    """
    try:
        import matplotlib.pyplot as plt

        n = len(images)
        fig, axes = plt.subplots(1, n, figsize=figsize)

        if n == 1:
            axes = [axes]

        for i in range(n):
            if len(images[i].shape) == 2:  # Grayscale
                axes[i].imshow(images[i], cmap=cmap)
            else:  # Color (BGR to RGB)
                axes[i].imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))

            axes[i].set_title(titles[i], fontsize=14, fontweight='bold', pad=10)
            axes[i].axis('off')

        plt.tight_layout()
        plt.show()

    except ImportError:
        print("Matplotlib not available - cannot display images")
        print("Install with: pip install matplotlib")

def main():
    """CLI entry point for RobustDocOCR."""
    import argparse
    import sys
    from utils.image_utils import load_image

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
