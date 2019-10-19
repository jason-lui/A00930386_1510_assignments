from unittest import TestCase
from unittest.mock import patch
from dungeonsanddragons import create_character


class TestCreate_character(TestCase):

    # Only test to see if create_character formats a character properly
    # Functions used in create_character have already been tested in their own unit tests
    # Therefore values are patched in
    @patch("dungeonsanddragons.roll_die", side_effect=[3, 3, 3, 3, 3, 3])
    @patch("dungeonsanddragons.select_class", return_value="monk")
    @patch("dungeonsanddragons.select_race", return_value="elf")
    @patch("dungeonsanddragons.roll_hp", return_value=[8, 8])
    @patch("dungeonsanddragons.generate_name", return_value="Jaxeno")
    def test_create_character_format(self, mock_name, mock_hp_roll, mock_race, mock_class, mock_roll):
        syllables = 3
        expected = {"Name": "Jaxeno", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": []}
        self.assertEqual(expected, create_character(syllables))
