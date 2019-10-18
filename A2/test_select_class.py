from unittest import TestCase
from unittest.mock import patch
from dungeonsanddragons import select_class
import io

class TestSelect_class(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value=1)
    def test_select_class_fighter(self, mock_class, mock_output):
        selected_class = "fighter"
        expected = """Select a class:
                   "1. Fighter
                   "2. Wizard
                   "3. Cleric
                   "4. Rogue
                   "5. Ranger
                    6. Barbarian
                    7. Bard
                    8. Druid
                    9. Monk
                    10. Paladin
                    11. Sorcerer
                    12. Warlock"""
        select_class()
        self.assertEqual(expected, mock_output.getvalue())

