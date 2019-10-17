from unittest import TestCase
from unittest.mock import patch
from lab05 import generate_name


class TestGenerate_name(TestCase):

    # Make sure the generated name is the correct length
    def test_generate_name_len(self):
        syllables = 10
        expected = 20
        self.assertEqual(expected, len(generate_name(syllables)))

    # Make sure the generated name is in title case
    def test_generate_name_title_case(self):
        syllables = 5
        name = generate_name(syllables)
        self.assertEqual(name, name.title())

    @patch("random.choice", side_effect=["b", "a", "d", "e", "h", "i"])
    def test_generate_name_1(self, mock_letter):
        syllables = 1
        expected = "Ba"
        self.assertEqual(expected, generate_name(syllables))

    @patch("random.choice", side_effect=["b", "a", "d", "e", "h", "i"])
    def test_generate_name_2(self, mock_letter):
        syllables = 2
        expected = "Bade"
        self.assertEqual(expected, generate_name(syllables))

    @patch("random.choice", side_effect=["b", "a", "d", "e", "h", "i"])
    def test_generate_name_3(self, mock_letter):
        syllables = 3
        expected = "Badehi"
        self.assertEqual(expected, generate_name(syllables))
