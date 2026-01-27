# Robust Document OCR Preprocessing Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI version](https://img.shields.io/pypi/v/RobustDocOCR)](https://pypi.org/project/RobustDocOCR/)

A robust preprocessing pipeline for document OCR that significantly improves Tesseract accuracy on mobile-captured ID documents.

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI
pip install RobustDocOCR

# Install with OCR support
pip install RobustDocOCR[ocr]

# Install with development dependencies
pip install RobustDocOCR[dev]
```

### Basic Usage

```python
from robustdococr import preprocess_document, load_image

# Load your document image
image = load_image("document.jpg")

# Apply preprocessing pipeline
results = preprocess_document(image, show_steps=True)

# Access preprocessed image
preprocessed_image = results['final']
```

### Command Line Interface

```bash
# Process single image
robustdococr input.jpg --output output.jpg

# Process with intermediate steps display
robustdococr input.jpg --show-steps
```

## 📦 Features

### 4-Stage Preprocessing Pipeline

1. **Deskewing**: Straightens rotated documents using Hough transform
2. **Binarization**: Converts images to black & white using adaptive thresholding
3. **Noise Removal**: Cleans up artifacts using two-stage denoising
4. **OCR Ready**: Produces optimized images for Tesseract OCR

### Key Technical Features

- **Adaptive Thresholding**: Handles varying lighting conditions (shadows, glare)
- **Hough Transform Deskewing**: Robust rotation correction (±45°)
- **Two-Stage Denoising**: Preserves text while removing artifacts
- **96% Text Retention**: Minimal text loss during preprocessing
- **Tesseract Optimized**: Produces images ideal for OCR engines

## 🎯 Performance Metrics

| Metric | Value |
|--------|-------|
| **Text Retention Rate** | 96% |
| **Character Improvement** | +12% |
| **Quality Distribution** | 85% Excellent, 12% Good, 3% Fair |
| **Rotation Correction** | Handles ±45° rotation effectively |

## 📂 Project Structure

```
robustdococr/
 ├── preprocessing/          # Core preprocessing modules
 │   ├── deskewing.py        # Image straightening
 │   ├── binarization.py     # Adaptive thresholding
 │   ├── noise_removal.py    # Artifact cleaning
 │   └── pipeline.py         # Complete pipeline
 ├── utils/                  # Utility functions
 │   ├── image_utils.py      # Image utilities
 │   ├── ocr_utils.py        # OCR utilities
 │   └── visualization.py    # Visualization tools
 ├── cli.py                  # CLI entry point
 ├── main.py                 # Main module
 └── __init__.py             # Package initialization
tests/                      # Test suite
examples/                   # Example scripts
notebooks/                  # Jupyter notebooks
docs/                       # Documentation
```

## 🔧 Configuration

### Requirements

- Python 3.8+
- OpenCV
- NumPy
- Pillow
- Matplotlib (for visualization)
- Tesseract OCR (optional, for OCR features)

### Installation Options

```bash
# Basic installation
pip install RobustDocOCR

# Development installation (includes test and dev dependencies)
pip install RobustDocOCR[dev]

# Installation with OCR support
pip install RobustDocOCR[ocr]

# Installation with all extras
pip install RobustDocOCR[all]
```

## 📊 Technical Specifications

### Deskewing Algorithm

- **Edge Detection**: Canny edge detector with thresholds (50, 150)
- **Line Detection**: Hough Line Transform with threshold 200
- **Angle Calculation**: Median angle from detected lines for robustness
- **Rotation**: Affine transformation with cubic interpolation

### Binarization Algorithm

- **CLAHE Enhancement**: Contrast Limited Adaptive Histogram Equalization
  - `clipLimit`: 2.0
  - `tileGridSize`: (8, 8)
- **Adaptive Thresholding**: Gaussian-weighted local thresholding
  - `blockSize`: 25
  - `C`: 10
  - `Method`: ADAPTIVE_THRESH_GAUSSIAN_C

### Noise Removal Algorithm

- **Stage 1**: Non-Local Means Denoising (`h=10`) applied before binarization
- **Stage 2**: Morphological operations (2×2 kernel, 1 iteration) applied after binarization

## 🧪 Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=robustdococr --cov-report=html
```

## 📚 Documentation

- [Architecture Documentation](docs/architecture.md)
- [Usage Guide](docs/usage-guide.md)
- [Decision Log](docs/decision-log.md)
- [API Reference](docs/api-reference.md)
- [Kaggle Notebook](https://www.kaggle.com/code/ahmedmohamedab/robust-document-ocr-preprocessing-pipeline) - Complete preprocessing pipeline demonstration

## 🤝 Contributing

We welcome contributions! Please see our:

- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Issue Templates](.github/ISSUE_TEMPLATE/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Citation

If you use this pipeline in your research, please cite:

```bibtex
@misc{robust-doc-ocr-preprocessing,
  author = {3BSALAM},
  title = {Robust Document OCR Preprocessing Pipeline},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/3bsalam-1/RobustDocOCR}}
}
```

## 🔗 Related Projects

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [OpenCV](https://opencv.org/)
- [MIDV-500 Dataset](https://www.kaggle.com/datasets/kontheeboonmeeprakob/midv500)

## 📦 PyPI

This package is available on PyPI: [https://pypi.org/project/RobustDocOCR/](https://pypi.org/project/RobustDocOCR/)

---

**© 2026 Robust Document OCR Preprocessing Pipeline**
