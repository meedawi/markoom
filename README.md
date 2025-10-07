# markoom (مرقوم) - Quran Analysis Library

[![PyPI version](https://badge.fury.io/py/markoom.svg)](https://badge.fury.io/py/markoom)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`markoom` is a Python library for the numerical and textual analysis of the Holy Quran. It provides a simple, intuitive, and powerful API to load Quranic text and perform various analyses, giving researchers precise control over text processing.

The name "Markoom" (مرقوم) is inspired by Surah Al-Mutaffifin, Ayah 20: "كِتَـٰبٌ مَّرْقُومٌ" (A register inscribed).

## Key Features

*   **Multiple Scripts**: Load the Quranic text in either **Uthmani** (`uthmani`) or **Simple/Imla'i** (`simple`) script.
*   **Intuitive API**: Access the text through a clean, object-oriented interface: `Quran`, `Surah`, and `Ayah`.
*   **Configurable Analysis**:
    *   **Character Normalization**: Group variants of letters (e.g., `أ`, `إ`, `آ` into `ا`).
    *   **Diacritic Removal**: Analyze text with or without Tashkeel (vowels).
    *   **Word Tokenization**: Define what constitutes a "word" by choosing whether to split attached conjunctions like 'و' and 'ف'.
*   **Zero Dependencies**: The library is lightweight and requires no external packages, making installation easy and reliable.
*   **Verified Data**: Uses the highly verified Quranic text from the [Tanzil Project](http://tanzil.net).

## License and Data Integrity

The Python source code for this library is released under the permissive **MIT License** (see the `LICENSE` file for details).

The Quranic text data files included with this library are sourced from the Tanzil Project. To ensure the sanctity and integrity of the Holy Quran, **modifying these data files (`quran-uthmani-min.xml` and `quran-simple-clean.xml`) is strictly prohibited.** Please read the `NOTICE` file for the full data usage policy.

## Installation

You can install `markoom` directly from the Python Package Index (PyPI):

```bash
pip install markoom


