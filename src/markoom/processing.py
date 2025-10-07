"""
This module provides functions for processing and normalizing Arabic text
from the Quran. It handles tasks like removing diacritics, normalizing
characters, and tokenizing text into words.
"""

import re

# A comprehensive list of Arabic diacritics to be removed
ARABIC_DIACRITICS = re.compile(r"""
                             ّ    | # Shadda
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)

# Normalization mapping for Arabic characters
ARABIC_NORMALIZATION_MAP = {
    'أ': 'ا', 'إ': 'ا', 'آ': 'ا',  # Normalize Hamza forms to Alif
    'ة': 'ه',                     # Normalize Ta Marbuta to Ha
    'ى': 'ي'                      # Normalize Alif Maqsura to Ya
}

def remove_diacritics(text: str) -> str:
    """
    Removes Arabic diacritics (Tashkeel) from a given text.

    :param text: The input string with diacritics.
    :return: The text with all diacritics removed.
    """
    return re.sub(ARABIC_DIACRITICS, '', text)

def normalize_arabic(text: str) -> str:
    """
    Normalizes Arabic characters to a common form.
    - Converts various forms of Alif (أ, إ, آ) to a plain Alif (ا).
    - Converts Ta Marbuta (ة) to Ha (ه).
    - Converts Alif Maqsura (ى) to Ya (ي).

    :param text: The input string.
    :return: The normalized string.
    """
    return ''.join([ARABIC_NORMALIZATION_MAP.get(char, char) for char in text])

def tokenize(text: str, split_on_wa: bool = False) -> list[str]:
    """
    Splits a string of Arabic text into a list of words (tokens).

    :param text: The string to be tokenized.
    :param split_on_wa: If True, separates leading conjunctions 'و' (and)
                        and 'ف' (so) from the following word.
                        Default is False, where "والله" is one token.
                        If True, "والله" becomes ["و", "الله"].
    :return: A list of string tokens.
    """
    words = text.split()
    if not split_on_wa:
        return words
    
    tokens = []
    for word in words:
        # Split leading 'و' or 'ف' if the word is longer than one character
        if len(word) > 1 and word.startswith(('و', 'ف')):
            tokens.append(word[0])  # The conjunction
            tokens.append(word[1:])  # The rest of the word
        else:
            tokens.append(word)
    return tokens