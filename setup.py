# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 11:52:04 2026

@author: gzche
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sinographic-translator",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for converting English words to Chinese characters based on roots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sinographic-translator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
    ],
    include_package_data=True,
    package_data={
        "sinographic_translator": ["data/*.csv", "data/*.json"],
    },
    entry_points={
        "console_scripts": [
            "sinographic=sinographic_translator.main:main",
        ],
    },
)