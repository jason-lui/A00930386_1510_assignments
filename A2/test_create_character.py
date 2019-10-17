from unittest import TestCase
from unittest.mock import patch
from lab05 import create_character


class TestCreate_character(TestCase):

    @patch("lab05.roll_die", side_effect=[1, 2, 3, 4, 5, 6])
    @patch("random.choice", side_effect=["b", "a", "d", "e", "h", "i"])
    def test_create_character_1(self, mock_letter, mock_roll):
        syllables = 1
        expected = ["Ba", ["Strength", 1], ["Dexterity", 2], ["Constitution", 3],
                              ["Intelligence", 4], ["Wisdom", 5], ["Charisma", 6]]
        self.assertEqual(expected, create_character(syllables))

    @patch("lab05.roll_die", side_effect=[6, 5, 4, 3, 2, 1])
    @patch("random.choice", side_effect=["b", "a", "d", "e", "h", "i"])
    def test_create_character_2(self, mock_letter, mock_roll):
        syllables = 2
        expected = ["Bade", ["Strength", 6], ["Dexterity", 5], ["Constitution", 4],
                              ["Intelligence", 3], ["Wisdom", 2], ["Charisma", 1]]
        self.assertEqual(expected, create_character(syllables))

    @patch("lab05.roll_die", side_effect=[3, 6, 9, 12, 15, 18])
    @patch("random.choice", side_effect=["b", "a", "d", "e", "h", "i"])
    def test_create_character_3(self, mock_letter, mock_roll):
        syllables = 3
        expected = ["Badehi", ["Strength", 3], ["Dexterity", 6], ["Constitution", 9],
                              ["Intelligence", 12], ["Wisdom", 15], ["Charisma", 18]]
        self.assertEqual(expected, create_character(syllables))
