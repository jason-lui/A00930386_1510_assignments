from unittest import TestCase
from maze import check_if_exit_reached


class TestCheck_if_exit_reached(TestCase):

    def test_check_if_exit_reached_true(self):
        char = {'coords': (4, 4)}
        expected = True
        self.assertEqual(expected, check_if_exit_reached(char))

    def test_check_if_exit_reached_false_4_0(self):
        char = {'coords': (4, 0)}
        expected = False
        self.assertEqual(expected, check_if_exit_reached(char))

    def test_check_if_exit_reached_false_0_4(self):
        char = {'coords': (0, 4)}
        expected = False
        self.assertEqual(expected, check_if_exit_reached(char))

    def test_check_if_exit_reached_false_0_0(self):
        char = {'coords': (0, 0)}
        expected = False
        self.assertEqual(expected, check_if_exit_reached(char))
