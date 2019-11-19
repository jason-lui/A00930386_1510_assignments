from unittest import TestCase
from question_7 import print_food_calories
from unittest.mock import patch
import io


class TestPrint_food_calories(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_food_calories_empty_dictionary(self, mock_output):
        test_food_dict = {}
        expected = ZeroDivisionError
        self.assertRaises(expected, print_food_calories, test_food_dict)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_food_calories(self, mock_output):
        test_food_dict = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66}
        expected = "\nFood Items: ['apple', 'bread', 'carrot', 'lettuce']\n" \
                   "Total Calories: 195 Average Calories: 48.8" \
                   "\n\n"
        print_food_calories(test_food_dict)
        self.assertEqual(expected, mock_output.getvalue())
