from unittest import TestCase
from unittest.mock import patch
from dungeonsanddragons import attack
import io


class TestAttack(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dungeonsanddragons.roll_die", return_value=1)
    def test_attack_hp_below_0(self, mock_roll, mock_output):
        player_1 = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        player_3 = {"Name": "Blake", "Class": "sorcerer", "Race": "human", "HP": [6, 0], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        expected = f"Blake is dead!\n"
        attack(player_3, player_1)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dungeonsanddragons.roll_die", return_value=1)
    def test_attack_fail(self, mock_roll, mock_output):
        player_1 = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        player_2 = {"Name": "Peachy", "Class": "monk", "Race": "elf", "HP": [8, 4], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        expected = "Peachy's HP: 4/8\n" \
                   "Ophelia's attack failed!\n" \
                   "Peachy's HP: 4/8\n\n"
        attack(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dungeonsanddragons.roll_die", side_effect=[20, 1])
    def test_attack_success(self, mock_roll, mock_output):
        player_1 = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        player_2 = {"Name": "Peachy", "Class": "monk", "Race": "elf", "HP": [8, 4], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        expected = "Peachy's HP: 4/8\n" \
                   "The attack was a success!\n" \
                   "Peachy took 1 damage.\n" \
                   "Peachy's HP: 3/8\n\n"
        attack(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dungeonsanddragons.roll_die", side_effect=[20, 8])
    def test_attack_kill(self, mock_roll, mock_output):
        player_1 = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        player_2 = {"Name": "Peachy", "Class": "monk", "Race": "elf", "HP": [8, 4], "Strength": 3, "Dexterity": 3,
                    "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
                    "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}
        expected = "Peachy's HP: 4/8\n" \
                   "The attack was a success!\n" \
                   "Peachy took 8 damage.\n" \
                   "Peachy has died!\n"
        attack(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())
