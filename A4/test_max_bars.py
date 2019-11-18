from unittest import TestCase
from question_8 import max_bars


class TestMax_bars(TestCase):

    def test_max_bars_1_12(self):
        test_lower_bound = 1
        test_upper_bound = 12
        expected = 10
        self.assertEqual(expected, max_bars(test_lower_bound, test_upper_bound))

    def test_max_bars_0_5(self):
        test_lower_bound = 0
        test_upper_bound = 5
        expected = 0
        self.assertEqual(expected, max_bars(test_lower_bound, test_upper_bound))

    def test_max_bars_0_9(self):
        test_lower_bound = 0
        test_upper_bound = 9
        expected = 8
        self.assertEqual(expected, max_bars(test_lower_bound, test_upper_bound))
