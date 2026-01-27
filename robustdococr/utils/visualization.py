"""Visualization utilities for OCR preprocessing results.

This module provides functions for creating visualizations of preprocessing
results and performance metrics.
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_comparison(batch_results):
    """Create comparison plots for batch processing results.

    Args:
        batch_results (list): List of batch processing results

    Returns:
        matplotlib.figure.Figure: Generated figure
    """
    if not batch_results:
        raise ValueError("No batch results provided")

    # Prepare data for plotting
    image_numbers = list(range(1, len(batch_results) + 1))
    chars_before = [r['chars_before'] for r in batch_results]
    chars_after = [r['chars_after'] for r in batch_results]
    retention_rates = [r['retention'] for r in batch_results]

    # Calculate dynamic y-axis limits
    max_retention = max(retention_rates) if retention_rates else 100
    ylim_upper = max(110, max_retention + 10)  # Ensure minimum 110%, add 10% padding

    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Plot 1: Character count comparison
    x = np.arange(len(batch_results))
    width = 0.35

    bars1 = ax1.bar(x - width/2, chars_before, width, label='Before', alpha=0.8, color='#FF6B6B')
    bars2 = ax1.bar(x + width/2, chars_after, width, label='After', alpha=0.8, color='#4ECDC4')

    ax1.set_xlabel('Image Number', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Characters Detected', fontsize=12, fontweight='bold')
    ax1.set_title('OCR Performance: Before vs After Preprocessing', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels([f'Img {i}' for i in image_numbers])
    ax1.legend(fontsize=11)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}', ha='center', va='bottom', fontsize=9)

    # Plot 2: Retention rates with dynamic scaling
    colors = ['#2ECC71' if r >= 95 else '#F39C12' if r >= 85 else '#E74C3C'
              for r in retention_rates]
    bars3 = ax2.bar(image_numbers, retention_rates, alpha=0.8, color=colors)

    # Add reference lines (only if within visible range)
    ax2.axhline(y=95, color='green', linestyle='--', linewidth=2, alpha=0.5, label='Excellent (95%)')
    ax2.axhline(y=85, color='orange', linestyle='--', linewidth=2, alpha=0.5, label='Good (85%)')
    ax2.axhline(y=70, color='red', linestyle='--', linewidth=2, alpha=0.5, label='Fair (70%)')

    ax2.set_xlabel('Image Number', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Text Retention Rate (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Text Preservation Quality', fontsize=14, fontweight='bold')
    ax2.set_xticks(image_numbers)
    ax2.set_xticklabels([f'Img {i}' for i in image_numbers])
    ax2.set_ylim(0, ylim_upper)  # Dynamic upper limit
    ax2.legend(fontsize=9, loc='lower right')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels with bounds checking
    for bar in bars3:
        height = bar.get_height()
        # Position label slightly below bar top if it would exceed chart bounds
        label_y = min(height, ylim_upper - 5)
        ax2.text(bar.get_x() + bar.get_width()/2., label_y,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()

    return fig

def plot_quality_distribution(batch_results):
    """Create quality distribution plot for batch results.

    Args:
        batch_results (list): List of batch processing results

    Returns:
        matplotlib.figure.Figure: Generated figure
    """
    if not batch_results:
        raise ValueError("No batch results provided")

    # Count quality levels
    excellent = sum(1 for r in batch_results if r['retention'] >= 95)
    good = sum(1 for r in batch_results if 85 <= r['retention'] < 95)
    fair = sum(1 for r in batch_results if 70 <= r['retention'] < 85)
    poor = sum(1 for r in batch_results if r['retention'] < 70)

    categories = ['Excellent', 'Good', 'Fair', 'Poor']
    counts = [excellent, good, fair, poor]
    colors = ['#2ECC71', '#F39C12', '#E74C3C', '#C0392B']

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(categories, counts, color=colors, alpha=0.8)

    ax.set_xlabel('Quality Level', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Images', fontsize=12, fontweight='bold')
    ax.set_title('Quality Distribution Across Processed Images', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontsize=11, fontweight='bold')

    plt.tight_layout()

    return fig