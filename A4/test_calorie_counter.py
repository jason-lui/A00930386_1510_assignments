from unittest import TestCase
from question_7 import calorie_counter
from unittest.mock import patch
import io


class TestCalorie_counter(TestCase):

    @patch('builtins.input', side_effect=['q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calorie_counter_instant_quit(self, mock_output, mock_input):
        expected = ""
        calorie_counter()
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['banana', '50', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calorie_counter_instant_add_1_item_then_quit(self, mock_output, mock_input):
        expected = "\n" \
                   "Food Items: ['apple', 'banana', 'beef', 'bread', 'butter', 'carrot', 'cheese', " \
                   "'chicken', 'lettuce', 'milk', 'pasta', 'rice', 'yogurt']\n" \
                   "Total Calories: 1555 Average Calories: 119.6" \
                   "\n\n"
        calorie_counter()
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['banana', '50', 'ice', '0', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calorie_counter_instant_add_2_items_then_quit(self, mock_output, mock_input):
        expected = "\n" \
                   "Food Items: ['apple', 'banana', 'beef', 'bread', 'butter', 'carrot', 'cheese', " \
                   "'chicken', 'lettuce', 'milk', 'pasta', 'rice', 'yogurt']\n" \
                   "Total Calories: 1555 Average Calories: 119.6" \
                   "\n\n" \
                   "\nFood Items: ['apple', 'banana', 'beef', 'bread', 'butter', 'carrot', 'cheese', " \
                   "'chicken', 'ice', 'lettuce', 'milk', 'pasta', 'rice', 'yogurt']\n" \
                   "Total Calories: 1555 Average Calories: 111.1" \
                   "\n\n"
        calorie_counter()
        self.assertEqual(expected, mock_output.getvalue())
