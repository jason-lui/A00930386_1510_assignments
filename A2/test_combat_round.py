from unittest import TestCase
from unittest.mock import patch
from dungeonsanddragons import combat_round
import io


class TestCombat_round(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dungeonsanddragons.roll_die", side_effect=[20, 1, 1, 1])
    def test_combat_round_double_fail(self, mock_roll, mock_output):
        player_1 = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        player_2 = {"Name": "Peachy", "Class": "monk", "Race": "elf", "HP": [8, 6], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        expected = """
Ophelia will go first.
Peachy's HP: 6/8
Ophelia's attack failed!
Peachy's HP: 6/8

Ophelia's HP: 8/8
Peachy's attack failed!
Ophelia's HP: 8/8

"""
        combat_round(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dungeonsanddragons.roll_die", side_effect=[20, 1, 1, 4, 1])
    def test_combat_round_fail_hit(self, mock_roll, mock_output):
        player_1 = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        player_2 = {"Name": "Peachy", "Class": "monk", "Race": "elf", "HP": [8, 6], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        expected = """
Ophelia will go first.
Peachy's HP: 6/8
Ophelia's attack failed!
Peachy's HP: 6/8

Ophelia's HP: 8/8
The attack was a success!
Ophelia took 1 damage.
Ophelia's HP: 7/8

"""
        combat_round(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dungeonsanddragons.roll_die", side_effect=[20, 1, 4, 1, 1])
    def test_combat_round_hit_fail(self, mock_roll, mock_output):
        player_1 = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        player_2 = {"Name": "Peachy", "Class": "monk", "Race": "elf", "HP": [8, 6], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        expected = """
Ophelia will go first.
Peachy's HP: 6/8
The attack was a success!
Peachy took 1 damage.
Peachy's HP: 5/8

Ophelia's HP: 8/8
Peachy's attack failed!
Ophelia's HP: 8/8

"""
        combat_round(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dungeonsanddragons.roll_die", side_effect=[20, 1, 4, 1, 4, 1])
    def test_combat_round_hit_hit(self, mock_roll, mock_output):
        player_1 = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        player_2 = {"Name": "Peachy", "Class": "monk", "Race": "elf", "HP": [8, 6], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        expected = """
Ophelia will go first.
Peachy's HP: 6/8
The attack was a success!
Peachy took 1 damage.
Peachy's HP: 5/8

Ophelia's HP: 8/8
The attack was a success!
Ophelia took 1 damage.
Ophelia's HP: 7/8

"""
        combat_round(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dungeonsanddragons.roll_die", side_effect=[20, 1, 4, 8])
    def test_combat_round_kill(self, mock_roll, mock_output):
        player_1 = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        player_2 = {"Name": "Peachy", "Class": "monk", "Race": "elf", "HP": [8, 6], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        expected = """
Ophelia will go first.
Peachy's HP: 6/8
The attack was a success!
Peachy took 8 damage.
Peachy has died!
Peachy is dead!
"""
        combat_round(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dungeonsanddragons.roll_die", side_effect=[20, 1, 1, 4, 8])
    def test_combat_round_fail_kill(self, mock_roll, mock_output):
        player_1 = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        player_2 = {"Name": "Peachy", "Class": "monk", "Race": "elf", "HP": [8, 6], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        expected = """
Ophelia will go first.
Peachy's HP: 6/8
Ophelia's attack failed!
Peachy's HP: 6/8

Ophelia's HP: 8/8
The attack was a success!
Ophelia took 8 damage.
Ophelia has died!
"""
        combat_round(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())
