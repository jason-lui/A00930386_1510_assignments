from unittest import TestCase
from lab05 import generate_vowel

vowels = ["a", "e", "i", "o", "u", "y"]


class TestGenerate_vowel(TestCase):

    # Make sure the generated string is a vowel
    def test_generate_vowel(self):
        self.assertTrue(generate_vowel() in vowels)

    # Make sure the generated string is a single character
    def test_generate_vowel_len(self):
        self.assertEqual(1, len(generate_vowel()))
