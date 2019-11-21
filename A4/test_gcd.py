from unittest import TestCase
from question_2 import gcd


class TestGcd(TestCase):

    def test_gcd_exception(self):
        test_a = 0
        test_b = 0
        expected = ZeroDivisionError
        self.assertRaises(expected, gcd, test_a, test_b)

    def test_gcd_exception_5_0(self):
        test_a = 5
        test_b = 0
        expected = ZeroDivisionError
        self.assertRaises(expected, gcd, test_a, test_b)

    def test_gcd_exception_neg5_0(self):
        test_a = -5
        test_b = 0
        expected = ZeroDivisionError
        self.assertRaises(expected, gcd, test_a, test_b)

    def test_gcd_30_12(self):
        test_a = 30
        test_b = 12
        expected = 6
        self.assertEqual(expected, gcd(test_a, test_b))

    def test_gcd_36_123(self):
        test_a = 36
        test_b = 123
        expected = 3
        self.assertEqual(expected, gcd(test_a, test_b))

    def test_gcd_neg36_123(self):
        test_a = -36
        test_b = 123
        expected = 3
        self.assertEqual(expected, gcd(test_a, test_b))

    def test_gcd_neg36_neg123(self):
        test_a = -36
        test_b = -123
        expected = 3
        self.assertEqual(expected, gcd(test_a, test_b))

    def test_gcd_same_num(self):
        test_a = 7
        test_b = 7
        expected = 7
        self.assertEqual(expected, gcd(test_a, test_b))

    def test_gcd_alias(self):
        test_a = 7
        expected = 7
        self.assertEqual(expected, gcd(test_a, test_a))
