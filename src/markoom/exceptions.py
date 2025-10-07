"""
This module defines custom exceptions used throughout the markoom library
to provide specific and clear error messages.
"""

class MarkoomError(Exception):
    """Base exception class for all errors related to the markoom library."""
    pass

class InvalidSurahNumberError(MarkoomError):
    """Raised when a non-existent Surah number (not between 1 and 114) is requested."""
    def __init__(self, surah_number):
        super().__init__(f"Invalid Surah number: {surah_number}. Must be between 1 and 114.")

class InvalidAyahNumberError(MarkoomError):
    """Raised when a non-existent Ayah number for a given Surah is requested."""
    def __init__(self, surah_number, ayah_number):
        super().__init__(f"Invalid Ayah number: {ayah_number} for Surah {surah_number}.")

class DataFileError(MarkoomError):
    """Raised when the required Quran XML data file cannot be found."""
    def __init__(self, file_path):
        super().__init__(f"Quran data file not found at: {file_path}. Please ensure it is correctly placed.")