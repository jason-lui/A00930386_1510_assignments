from unittest import TestCase
from lab05 import generate_consonant

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


class TestGenerate_consonant(TestCase):

    # Make sure the generated string is a consonant
    def test_generate_consonant(self):
        self.assertTrue(generate_consonant() in consonants)

    # Make sure the generate string is a single character
    def test_generate_consonant_len(self):
        self.assertEqual(1, len(generate_consonant()))
