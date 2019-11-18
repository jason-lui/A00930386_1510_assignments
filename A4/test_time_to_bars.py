from unittest import TestCase
from question_8 import time_to_bars


class TestTime_to_bars(TestCase):

    def test_time_to_bars_10_08(self):
        test_time_str = "10:08"
        expected = 21
        self.assertEqual(expected, time_to_bars(test_time_str))

    def test_time_to_bars_1_23(self):
        test_time_str = "1:23"
        expected = 12
        self.assertEqual(expected, time_to_bars(test_time_str))

    def test_time_to_bars_4_56(self):
        test_time_str = "4:56"
        expected = 15
        self.assertEqual(expected, time_to_bars(test_time_str))

    def test_time_to_bars_empty(self):
        test_time_str = ""
        expected = 0
        self.assertEqual(expected, time_to_bars(test_time_str))
