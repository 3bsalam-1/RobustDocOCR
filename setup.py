#!/usr/bin/env python3
"""Setup script for RobustDocOCR package."""

import os
from pathlib import Path

from setuptools import find_packages, setup

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Package version
version = "1.0.3"

# Development requirements
dev_requires = [
    "pytest>=7.0.0",
    "pytest-cov>=3.0.0",
    "black>=22.0.0",
    "flake8>=4.0.0",
    "isort>=5.0.0",
    "mypy>=0.900",
    "twine>=4.0.0",
    "build>=0.8.0",
]

# OCR requirements
ocr_requires = [
    "pytesseract>=0.3.0",
]

setup(
    name="RobustDocOCR",
    version=version,
    description="A robust preprocessing pipeline for document OCR that significantly improves Tesseract accuracy on mobile-captured ID documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ahmed Mohamed",
    author_email="3bsalam0@gmail.com",
    url="https://github.com/3bsalam-1/RobustDocOCR",
    project_urls={
        "Bug Tracker": "https://github.com/3bsalam-1/RobustDocOCR/issues",
        "Documentation": "https://github.com/3bsalam-1/RobustDocOCR/blob/main/docs",
        "Source Code": "https://github.com/3bsalam-1/RobustDocOCR",
        "LinkedIn": "https://www.linkedin.com/in/ahmed-abdulsalam1",
    },
    packages=find_packages(exclude=["src*", "tests*", "examples*", "notebooks*", "scripts*", "docs*"]),
    package_dir={"": "."},
    package_data={
        "robustdococr": ["py.typed"],
    },
    include_package_data=True,
    extras_require={
        "dev": dev_requires,
        "ocr": ocr_requires,
        "all": dev_requires + ocr_requires,
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    entry_points={
        "console_scripts": [
            "robustdococr=robustdococr.cli:main",
        ],
    },
    license="MIT",
    zip_safe=False,
)