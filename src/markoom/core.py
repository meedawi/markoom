"""
This module contains the core classes for the markoom library.
The Quran class is the main entry point for loading and accessing Quranic data.
The Surah and Ayah classes model the structure of the Quran and provide
methods for numerical analysis.
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict

# Import local modules
from . import processing
from . import exceptions

class Ayah:
    """
    Represents a single Ayah (verse) of the Quran.
    
    This class stores the raw text of the verse and provides methods
    to perform various text analyses on it.
    """
    def __init__(self, surah_number: int, number: int, text: str):
        self.surah_number = surah_number
        self.number = number
        self.raw_text = text

    def __repr__(self) -> str:
        return f"<Ayah {self.surah_number}:{self.number}>"

    def get_processed_text(self, normalize: bool = True, remove_diacritics: bool = True) -> str:
        """
        Returns a processed version of the Ayah's text.

        :param normalize: If True, normalizes Arabic characters (e.g., 'أ' -> 'ا').
        :param remove_diacritics: If True, removes all Tashkeel.
        :return: The processed text as a string.
        """
        text = self.raw_text
        if remove_diacritics:
            text = processing.remove_diacritics(text)
        if normalize:
            text = processing.normalize_arabic(text)
        return text

    def get_words(self, **kwargs) -> List[str]:
        """
        Returns a list of words from the Ayah, with processing options.

        :param normalize: (bool) Passed to get_processed_text.
        :param remove_diacritics: (bool) Passed to get_processed_text.
        :param split_on_wa: (bool) If True, splits leading 'و' and 'ف'.
        :return: A list of words.
        """
        text_to_tokenize = self.get_processed_text(
            normalize=kwargs.get('normalize', True),
            remove_diacritics=kwargs.get('remove_diacritics', True)
        )
        return processing.tokenize(
            text_to_tokenize,
            split_on_wa=kwargs.get('split_on_wa', False)
        )

    def word_count(self, **kwargs) -> int:
        """Counts the number of words in the Ayah with processing options."""
        return len(self.get_words(**kwargs))

    def letter_count(self, **kwargs) -> int:
        """Counts the number of letters in the Ayah with processing options."""
        processed_text = self.get_processed_text(**kwargs)
        # Remove spaces to count only letters
        return len(processed_text.replace(' ', ''))

class Surah:
    """
    Represents a single Surah (chapter) of the Quran.
    
    It contains a collection of Ayah objects and provides methods for
    analysis across the entire Surah.
    """
    def __init__(self, number: int, name: str, ayahs: List[Ayah]):
        self.number = number
        self.name = name
        self.ayahs = ayahs

    def __repr__(self) -> str:
        return f"<Surah {self.number}: {self.name}>"

    def get_ayah(self, ayah_number: int) -> Ayah:
        """
        Retrieves an Ayah from this Surah by its number.

        :param ayah_number: The number of the Ayah (1-indexed).
        :return: The Ayah object.
        :raises InvalidAyahNumberError: If the number is out of bounds.
        """
        if 1 <= ayah_number <= len(self.ayahs):
            return self.ayahs[ayah_number - 1]  # Adjust for 0-based list index
        raise exceptions.InvalidAyahNumberError(self.number, ayah_number)

    def word_count(self, **kwargs) -> int:
        """Counts the total number of words in the Surah with processing options."""
        return sum(ayah.word_count(**kwargs) for ayah in self.ayahs)

    def letter_count(self, **kwargs) -> int:
        """Counts the total number of letters in the Surah with processing options."""
        return sum(ayah.letter_count(**kwargs) for ayah in self.ayahs)

class Quran:
    """
    The main class for interacting with the Quranic text.
    
    This class loads the Quran from a specified XML script file and provides
    access to its Surahs and Ayahs.
    """
    def __init__(self, script: str = 'uthmani'):
        """
        Initializes and loads the Quranic text.

        :param script: The script to load. Can be 'uthmani' (default) or 'simple'.
        :raises DataFileError: If the XML file for the script is not found.
        """
        if script not in ['uthmani', 'simple']:
            raise ValueError("Script must be either 'uthmani' or 'simple'.")
        
        self.script = script
        self._surahs: Dict[int, Surah] = {}
        self._load_data()

    def _load_data(self):
        """Parses the XML data file and populates the Surah objects."""
        if self.script == 'uthmani':
            file_name = f'quran-{self.script}-min.xml'
        else:
            file_name = f'quran-{self.script}-clean.xml'
        file_name = f'quran-{self.script}-min.xml'
        file_path = Path(__file__).parent / 'data' / file_name
        
        if not file_path.exists():
            raise exceptions.DataFileError(file_path)

        tree = ET.parse(file_path)
        root = tree.getroot()

        for sura_element in root.findall('sura'):
            sura_number = int(sura_element.get('index'))
            sura_name = sura_element.get('name')
            
            ayahs_list = []
            for aya_element in sura_element.findall('aya'):
                ayah_number = int(aya_element.get('index'))
                ayah_text = aya_element.get('text')
                
                # Prepend Bismillah if it exists as an attribute (e.g., in Surah At-Tawbah)
                if 'bismillah' in aya_element.attrib and aya_element == sura_element.find('aya'):
                     ayah_text = aya_element.get('bismillah') + " " + ayah_text
                
                ayahs_list.append(Ayah(sura_number, ayah_number, ayah_text))
            
            self._surahs[sura_number] = Surah(sura_number, sura_name, ayahs_list)

    def get_surah(self, surah_number: int) -> Surah:
        """
        Retrieves a Surah by its number.

        :param surah_number: The number of the Surah (1-114).
        :return: The Surah object.
        :raises InvalidSurahNumberError: If the number is out of bounds.
        """
        surah = self._surahs.get(surah_number)
        if surah is None:
            raise exceptions.InvalidSurahNumberError(surah_number)
        return surah

    def get_ayah(self, surah_number: int, ayah_number: int) -> Ayah:
        """
        A convenience method to retrieve an Ayah directly by its Surah and Ayah number.
        
        :param surah_number: The number of the Surah (1-114).
        :param ayah_number: The number of the Ayah.
        :return: The Ayah object.
        """
        surah = self.get_surah(surah_number)
        return surah.get_ayah(ayah_number)