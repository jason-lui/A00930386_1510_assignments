from unittest import TestCase
from lab05 import generate_syllable

vowels = ["a", "e", "i", "o", "u", "y"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


class TestGenerate_syllable(TestCase):

    # Make sure that the syllable is the correct length
    def test_generate_syllable_len(self):
        syllable = generate_syllable()
        self.assertEqual(2, len(syllable))

    # Make sure that the consonant appears before the vowel
    def test_generate_syllable_order(self):
        syllable = generate_syllable()
        self.assertTrue(syllable[0] in consonants and syllable[1] in vowels)

    # Make sure that syllables contain letters only
    def test_generate_syllable_alpha(self):
        self.assertTrue(generate_syllable().isalpha())
