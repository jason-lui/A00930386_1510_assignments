from unittest import TestCase
from maze import make_character


class TestMake_character(TestCase):

    def test_make_character(self):
        expected = {'coords': (0, 0)}
        self.assertEqual(expected, make_character())
