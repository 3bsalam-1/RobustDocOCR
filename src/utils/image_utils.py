"""Image utility functions for document processing.

This module provides helper functions for loading, displaying, and processing
document images.
"""

import cv2
import os

def load_image(image_path):
    """Load image from path with error handling.

    Args:
        image_path (str): Path to image file

    Returns:
        numpy.ndarray: Loaded image

    Raises:
        ValueError: If image cannot be loaded
        FileNotFoundError: If file does not exist
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not load image from {image_path}")

    return img

def display_images(images, titles, figsize=(20, 8), cmap='gray'):
    """Display multiple images in a row with titles.

    Args:
        images (list): List of images to display
        titles (list): List of titles for each image
        figsize (tuple): Figure size (width, height)
        cmap (str): Colormap for grayscale images

    Raises:
        ImportError: If matplotlib is not available
        ValueError: If images and titles lists have different lengths
    """
    try:
        import matplotlib.pyplot as plt

        if len(images) != len(titles):
            raise ValueError("Images and titles lists must have the same length")

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

def print_section_header(title):
    """Print formatted section header.

    Args:
        title (str): Section title to print
    """
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)