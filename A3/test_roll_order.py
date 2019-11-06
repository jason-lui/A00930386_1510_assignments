from unittest import TestCase
from unittest.mock import patch
from sud import roll_order
import io

player_1 = {"Name": "Ophelia", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
            "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
            "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}

player_2 = {"Name": "Peachy", "Class": "monk", "Race": "elf", "HP": [8, 8], "Strength": 3, "Dexterity": 3,
            "Constitution": 3, "Intelligence": 3, "Wisdom": 3, "Charisma": 3, "XP": 0,
            "Inventory": ["Boots of Swiftness", "Boots of Alacrity"]}


class TestRoll_order(TestCase):

    # Randomly generated order is either p1 > p2 or p2 > p1
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_roll_order_same_roll_random(self, mock_output):
        possible = [[player_1, player_2], [player_2, player_1]]
        order = roll_order(player_1, player_2)
        self.assertIn(order, possible)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[20, 1])
    def test_roll_order_player_1_print(self, mock_roll, mock_output):
        expected = "\nOphelia will go first.\n"
        order = roll_order(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[20, 1])
    def test_roll_order_player_1_return(self, mock_roll, mock_output):
        expected = [player_1, player_2]
        order = roll_order(player_1, player_2)
        self.assertEqual(expected, order)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[1, 20])
    def test_roll_order_player_2_print(self, mock_roll, mock_output):
        expected = "\nPeachy will go first.\n"
        order = roll_order(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[1, 20])
    def test_roll_order_player_2_return(self, mock_roll, mock_output):
        expected = [player_2, player_1]
        order = roll_order(player_1, player_2)
        self.assertEqual(expected, order)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[1, 1, 20, 1])
    def test_roll_order_same_then_p1_print(self, mock_roll, mock_output):
        expected = "Both players rolled 1! Rolling again...\n" \
                   "\nOphelia will go first.\n"
        order = roll_order(player_1, player_2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[1, 1, 20, 1])
    def test_roll_order_same_roll_then_p1_return(self, mock_roll, mock_output):
        expected = [player_1, player_2]
        order = roll_order(player_1, player_2)
        self.assertEqual(expected, order)
