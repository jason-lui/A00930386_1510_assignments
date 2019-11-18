from unittest import TestCase
from question_1 import eratosthenes


class TestEratosthenes(TestCase):

    def test_eratosthenes_exception_negative(self):
        upper_bound = -1
        expected = Exception
        self.assertRaises(expected, eratosthenes, upper_bound)

    def test_eratosthenes_exception_0(self):
        upper_bound = 0
        expected = Exception
        self.assertRaises(expected, eratosthenes, upper_bound)

    def test_eratosthenes_exception_1(self):
        upper_bound = 1
        expected = []
        self.assertEqual(expected, eratosthenes(upper_bound))

    def test_eratosthenes_exception_2(self):
        upper_bound = 2
        expected = [2]
        self.assertEqual(expected, eratosthenes(upper_bound))

    def test_eratosthenes_exception_30(self):
        upper_bound = 30
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(expected, eratosthenes(upper_bound))
