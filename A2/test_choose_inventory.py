from unittest import TestCase
from unittest.mock import patch
from lab05 import choose_inventory
import io


class TestChoose_inventory(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_0_0(self, mock_items, mock_output):
        inventory = []
        selection = 0
        expected = []
        self.assertEqual(expected, choose_inventory(inventory, selection))

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_4_0(self, mock_items, mock_output):
        inventory = ['Rabadon\'s Deathcap', 'Abyssal\' Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        selection = 0
        expected = []
        self.assertEqual(expected, choose_inventory(inventory, selection))

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_0_n1_value(self, mock_items, mock_output):
        inventory = []
        selection = -1
        expected = []
        self.assertEqual(expected, choose_inventory(inventory, selection))

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_0_n1_print(self, mock_items, mock_output):
        inventory = []
        selection = -1
        expected = "WARNING: The number of items selected is negative.\n"
        choose_inventory(inventory, selection)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_4_n1_value(self, mock_items, mock_output):
        inventory = ['Rabadon\'s Deathcap', 'Abyssal\' Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        selection = -1
        expected = []
        self.assertEqual(expected, choose_inventory(inventory, selection))

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_4_n1_print(self, mock_items, mock_output):
        inventory = ['Rabadon\'s Deathcap', 'Abyssal\' Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        selection = -1
        expected = "WARNING: The number of items selected is negative.\n"
        choose_inventory(inventory, selection)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_0_4_value(self, mock_items, mock_output):
        inventory = []
        selection = 4
        expected = []
        self.assertEqual(expected, choose_inventory(inventory, selection))

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_0_4_print(self, mock_items, mock_output):
        inventory = []
        selection = 4
        expected = "WARNING: The number of items selected is larger than the size of the inventory.\n"
        choose_inventory(inventory, selection)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[['Rapidfire Cannon', 'Boots of Lucidity']])
    def test_choose_inventory_4_2(self, mock_items, mock_output):
        inventory = ['Rabadon\'s Deathcap', 'Abyssal\' Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        selection = 2
        self.assertEqual(['Boots of Lucidity', 'Rapidfire Cannon'], choose_inventory(inventory, selection))
