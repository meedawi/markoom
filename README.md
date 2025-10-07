Of course. Here is a revised and comprehensive version of the `README.md` file, designed to be clear, welcoming, and informative for new users on GitHub and PyPI.

---

📄 **File: `README.md`**
```markdown
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
*   **Verified Data**: Uses the highly verified Quranic text from the [Tanzil Project](http.tanzil.net).

## License and Data Integrity

The Python source code for this library is released under the permissive **MIT License** (see the `LICENSE` file for details).

The Quranic text data files included with this library are sourced from the Tanzil Project. To ensure the sanctity and integrity of the Holy Quran, **modifying these data files (`quran-uthmani-min.xml` and `quran-simple-clean.xml`) is strictly prohibited.** Please read the `NOTICE` file for the full data usage policy.

## Installation

You can install `markoom` directly from the Python Package Index (PyPI):

```bash
pip install markoom
```

## Quick Start Guide

Here is a brief example demonstrating how to use the `markoom` library for basic analysis.

```python
import markoom

# 1. Initialize the library with the desired Quran script
quran = markoom.Quran(script='uthmani')

# 2. Get a Surah by its number (e.g., Surah 1, Al-Fatiha)
al_fatiha = quran.get_surah(1)
print(f"Analyzing Surah {al_fatiha.number}: {al_fatiha.name}")

# 3. Get a specific Ayah from the Surah
ayah_7 = al_fatiha.get_ayah(7)
print(f"\nRaw Text of Ayah {ayah_7.surah_number}:{ayah_7.number}:")
print(f"'{ayah_7.raw_text}'")

# 4. Perform default analysis (normalized, without diacritics)
word_count = ayah_7.word_count()
letter_count = ayah_7.letter_count()
print(f"\nThis Ayah has {word_count} words and {letter_count} letters (default processing).")

# 5. Use advanced options for more specific analysis
# Example: Count words, but split attached 'و' (wa)
word_count_split = ayah_7.word_count(split_on_wa=True)
words_split = ayah_7.get_words(split_on_wa=True)

print(f"\nWith 'wa' splitting, the word count is: {word_count_split}")
print(f"The words are: {words_split}")

# 6. Analyze an entire Surah
total_words_in_fatiha = al_fatiha.word_count()
print(f"\nTotal words in {al_fatiha.name}: {total_words_in_fatiha}")
```

## Contributing

Contributions, bug reports, and feature requests are welcome! Please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/your-username/markoom).
```
*(Note: Be sure to update the "Contributing" link to your actual GitHub repository URL once it is created.)*