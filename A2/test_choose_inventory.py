from unittest import TestCase
from unittest.mock import patch
from dungeonsanddragons import choose_inventory
import io


class TestChoose_inventory(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[1, 2, 3, 4, -1])
    def test_choose_inventory_4_items(self, mock_items, mock_output):
        sample = ['Rabadon\'s Deathcap', 'Abyssal\' Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        expected = "Welcome to the Olde Tyme Merchant!\n" \
                   "\n" \
                   "Here is what we have for sale:\n" \
                   "--Current Inventory--\n" \
                   "\n" \
                   "\n" \
                   "1. Rabadon\'s Deathcap\n" \
                   "2. Abyssal\' Mask\n" \
                   "3. Rapidfire Cannon\n" \
                   "4. Boots of Lucidity\n" \
                   "--Current Inventory--\n" \
                   "Rabadon\'s Deathcap\n" \
                   "\n" \
                   "\n" \
                   "1. Rabadon\'s Deathcap\n" \
                   "2. Abyssal\' Mask\n" \
                   "3. Rapidfire Cannon\n" \
                   "4. Boots of Lucidity\n" \
                   "--Current Inventory--\n" \
                   "Rabadon\'s Deathcap\n" \
                   "Abyssal\' Mask\n" \
                   "\n" \
                   "\n" \
                   "1. Rabadon\'s Deathcap\n" \
                   "2. Abyssal\' Mask\n" \
                   "3. Rapidfire Cannon\n" \
                   "4. Boots of Lucidity\n" \
                   "--Current Inventory--\n" \
                   "Rabadon\'s Deathcap\n" \
                   "Abyssal\' Mask\n" \
                   "Rapidfire Cannon\n" \
                   "\n" \
                   "\n" \
                   "1. Rabadon\'s Deathcap\n" \
                   "2. Abyssal\' Mask\n" \
                   "3. Rapidfire Cannon\n" \
                   "4. Boots of Lucidity\n" \
                   "--Current Inventory--\n" \
                   "Rabadon\'s Deathcap\n" \
                   "Abyssal\' Mask\n" \
                   "Rapidfire Cannon\n" \
                   "Boots of Lucidity\n" \
                   "\n" \
                   "\n" \
                   "1. Rabadon\'s Deathcap\n" \
                   "2. Abyssal\' Mask\n" \
                   "3. Rapidfire Cannon\n" \
                   "4. Boots of Lucidity\n"
        inventory = choose_inventory(sample)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[5, -1])
    def test_choose_inventory_error(self, mock_items, mock_output):
        sample = ['Rabadon\'s Deathcap', 'Abyssal\' Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        expected = "Welcome to the Olde Tyme Merchant!\n" \
                   "\n" \
                   "Here is what we have for sale:\n" \
                   "--Current Inventory--\n" \
                   "\n" \
                   "\n" \
                   "1. Rabadon's Deathcap\n" \
                   "2. Abyssal' Mask\n" \
                   "3. Rapidfire Cannon\n" \
                   "4. Boots of Lucidity\n" \
                   "You must enter a number corresponding to an item in the list.\n" \
                   "\n" \
                   "--Current Inventory--\n" \
                   "\n" \
                   "\n" \
                   "1. Rabadon's Deathcap\n" \
                   "2. Abyssal' Mask\n" \
                   "3. Rapidfire Cannon\n" \
                   "4. Boots of Lucidity\n"
        inventory = choose_inventory(sample)
        self.assertEqual(expected, mock_output.getvalue())