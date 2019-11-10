from unittest import TestCase
from unittest.mock import patch
from sud import attack
import io


class TestAttack(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", return_value=1)
    def test_attack_hp_below_0(self, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 0, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 5, 'power': 6, 'backstab': 4}
        expected = "Link is dead!"
        attack(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())
