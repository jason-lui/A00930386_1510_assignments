from unittest import TestCase
from maze import make_board


class TestMake_board(TestCase):

    def test_make_board(self):
        expected = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]
        self.assertEqual(expected, make_board())
