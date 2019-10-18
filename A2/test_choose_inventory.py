from unittest import TestCase
from unittest.mock import patch
from dungeonsanddragons import choose_inventory
import io


class TestChoose_inventory(TestCase):

    # Choose no items
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[-1])
    def test_choose_inventory_no_items_print(self, mock_items, mock_output):
        sample = ['Rabadon\'s Deathcap', 'Abyssal Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        expected = """Welcome to the Olde Tyme Merchant!

Here is what we have for sale:
--Current Inventory--


1. Rabadon's Deathcap
2. Abyssal Mask
3. Rapidfire Cannon
4. Boots of Lucidity
--Inventory--
"""
        inventory = choose_inventory(sample)
        self.assertEqual(expected, mock_output.getvalue())

    # Choose no items
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[-1])
    def test_choose_inventory_no_items_return(self, mock_items, mock_output):
        sample = ['Rabadon\'s Deathcap', 'Abyssal Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        expected = []
        inventory = choose_inventory(sample)
        self.assertEqual(expected, inventory)

    # Choose multiple of the same item
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[1, 1, -1])
    def test_choose_inventory_duplicate_print(self, mock_items, mock_output):
        sample = ['Rabadon\'s Deathcap', 'Abyssal Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        expected = """Welcome to the Olde Tyme Merchant!

Here is what we have for sale:
--Current Inventory--


1. Rabadon's Deathcap
2. Abyssal Mask
3. Rapidfire Cannon
4. Boots of Lucidity
--Current Inventory--
Rabadon's Deathcap


1. Rabadon's Deathcap
2. Abyssal Mask
3. Rapidfire Cannon
4. Boots of Lucidity
--Current Inventory--
Rabadon's Deathcap
Rabadon's Deathcap


1. Rabadon's Deathcap
2. Abyssal Mask
3. Rapidfire Cannon
4. Boots of Lucidity
--Inventory--
Rabadon's Deathcap
Rabadon's Deathcap
"""
        inventory = choose_inventory(sample)
        self.assertEqual(expected, mock_output.getvalue())

    # Choose multiple of the same item
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[1, 1, -1])
    def test_choose_inventory_duplicate_return(self, mock_items, mock_output):
        sample = ['Rabadon\'s Deathcap', 'Abyssal Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        expected = ['Rabadon\'s Deathcap', 'Rabadon\'s Deathcap']
        inventory = choose_inventory(sample)
        self.assertEqual(expected, inventory)

    # Choose all items
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[1, 2, 3, 4, -1])
    def test_choose_inventory_all_items_print(self, mock_items, mock_output):
        sample = ['Rabadon\'s Deathcap', 'Abyssal Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        expected = """Welcome to the Olde Tyme Merchant!

Here is what we have for sale:
--Current Inventory--


1. Rabadon's Deathcap
2. Abyssal Mask
3. Rapidfire Cannon
4. Boots of Lucidity
--Current Inventory--
Rabadon's Deathcap


1. Rabadon's Deathcap
2. Abyssal Mask
3. Rapidfire Cannon
4. Boots of Lucidity
--Current Inventory--
Rabadon's Deathcap
Abyssal Mask


1. Rabadon's Deathcap
2. Abyssal Mask
3. Rapidfire Cannon
4. Boots of Lucidity
--Current Inventory--
Rabadon's Deathcap
Abyssal Mask
Rapidfire Cannon


1. Rabadon's Deathcap
2. Abyssal Mask
3. Rapidfire Cannon
4. Boots of Lucidity
--Current Inventory--
Rabadon's Deathcap
Abyssal Mask
Rapidfire Cannon
Boots of Lucidity


1. Rabadon's Deathcap
2. Abyssal Mask
3. Rapidfire Cannon
4. Boots of Lucidity
--Inventory--
Rabadon's Deathcap
Abyssal Mask
Rapidfire Cannon
Boots of Lucidity
"""
        inventory = choose_inventory(sample)
        self.assertEqual(expected, mock_output.getvalue())

    # Choose all items
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[1, 2, 3, 4, -1])
    def test_choose_inventory_all_items_return(self, mock_items, mock_output):
        sample = ['Rabadon\'s Deathcap', 'Abyssal Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        expected = ['Rabadon\'s Deathcap', 'Abyssal Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        inventory = choose_inventory(sample)
        self.assertEqual(expected, inventory)

    # Choose a number outside of the list
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[5, -1])
    def test_choose_inventory_error(self, mock_items, mock_output):
        sample = ['Rabadon\'s Deathcap', 'Abyssal Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        expected = """Welcome to the Olde Tyme Merchant!

Here is what we have for sale:
--Current Inventory--


1. Rabadon's Deathcap
2. Abyssal Mask
3. Rapidfire Cannon
4. Boots of Lucidity
You must enter a number corresponding to an item in the list.

--Current Inventory--


1. Rabadon's Deathcap
2. Abyssal Mask
3. Rapidfire Cannon
4. Boots of Lucidity
--Inventory--
"""
        inventory = choose_inventory(sample)
        self.assertEqual(expected, mock_output.getvalue())
