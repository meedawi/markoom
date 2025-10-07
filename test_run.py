# To run this, you must be in the `markoom_project` directory
# and run `python -m test_run` or have `src` in your PYTHONPATH.
from src.markoom import Quran

# 1. Initialize the library
print("Loading Uthmani script...")
quran = Quran(script='uthmani')
print("Load complete.")

# 2. Get Surah Al-Fatiha
al_fatiha = quran.get_surah(1)
print(f"Surah: {al_fatiha.name}")

# 3. Get a specific Ayah and its text
ayah_5 = al_fatiha.get_ayah(5)
print(f"Ayah 1:5 (raw): '{ayah_5.raw_text}'")
print(f"Ayah 1:5 (processed): '{ayah_5.get_processed_text()}'")

# 4. Perform word count analysis
print("\n--- Word Count Analysis ---")
print(f"Default word count for Ayah 1:5 is: {ayah_5.word_count()}")
print(f"Word count for Ayah 1:5 (splitting 'wa'): {ayah_5.word_count(split_on_wa=True)}")
print(f"Words (splitting 'wa'): {ayah_5.get_words(split_on_wa=True)}")

# 5. Perform letter count analysis
print("\n--- Letter Count Analysis ---")
print(f"Letter count for Ayah 1:5 (default): {ayah_5.letter_count()}")
print(f"Letter count for Ayah 1:5 (with diacritics, no norm): {ayah_5.letter_count(normalize=False, remove_diacritics=False)}")

# 6. Analyze a whole Surah
print("\n--- Surah Level Analysis ---")
word_count_fatiha = al_fatiha.word_count()
letter_count_fatiha = al_fatiha.letter_count()
print(f"Surah Al-Fatiha has {word_count_fatiha} words and {letter_count_fatiha} letters.")