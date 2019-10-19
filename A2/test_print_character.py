from unittest import TestCase
from unittest.mock import patch
from dungeonsanddragons import print_character
import io


class TestPrint_character(TestCase):

    # A character without an inventory
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_no_inventory(self, mock_output):
        character = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                     "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0}
        expected = """
Your character's name is Ophelia.

Class: Monk
Race: Elf
HP: 8/8

--Attributes--
Strength: 3
Dexterity: 3
Constitution: 3
Intelligence: 3
Wisdom: 3
Charisma: 3

EXP: 0
"""
        print_character(character)
        self.assertEqual(expected, mock_output.getvalue())

    # A character with an inventory but no items
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_no_items(self, mock_output):
        character = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                     "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                     "Inventory": []}
        expected = """
Your character's name is Ophelia.

Class: Monk
Race: Elf
HP: 8/8

--Attributes--
Strength: 3
Dexterity: 3
Constitution: 3
Intelligence: 3
Wisdom: 3
Charisma: 3

EXP: 0

--Inventory--
You have no items...
"""
        print_character(character)
        self.assertEqual(expected, mock_output.getvalue())

    # A character with an inventory and items
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_items(self, mock_output):
        character = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                     "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                     "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        expected = """
Your character's name is Ophelia.

Class: Monk
Race: Elf
HP: 8/8

--Attributes--
Strength: 3
Dexterity: 3
Constitution: 3
Intelligence: 3
Wisdom: 3
Charisma: 3

EXP: 0

--Inventory--
Boots of Swiftness
Boots of Alacrity
"""
        print_character(character)
        self.assertEqual(expected, mock_output.getvalue())
