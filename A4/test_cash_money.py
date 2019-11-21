from unittest import TestCase
from question_5 import cash_money


class TestCash_money(TestCase):

    def test_cash_money_exception_negative(self):
        test_cad = -10.00
        expected = ValueError
        self.assertRaises(expected, cash_money, test_cad)

    def test_cash_money_exception(self):
        test_cad = 0
        expected = ValueError
        self.assertRaises(expected, cash_money, test_cad)

    def test_cash_money_0_01(self):
        test_cad = 0.01
        expected = {0.01: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_0_05(self):
        test_cad = 0.05
        expected = {0.05: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_0_10(self):
        test_cad = 0.10
        expected = {0.10: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_0_25(self):
        test_cad = 0.25
        expected = {0.25: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_1_00(self):
        test_cad = 1.00
        expected = {1: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_2_00(self):
        test_cad = 2.00
        expected = {2: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_5_00(self):
        test_cad = 5.00
        expected = {5: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_10_00(self):
        test_cad = 10.00
        expected = {10: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_20_00(self):
        test_cad = 20.00
        expected = {20: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_50_00(self):
        test_cad = 50.00
        expected = {50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_100_00(self):
        test_cad = 100.00
        expected = {100: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_183_45(self):
        test_cad = 183.45
        expected = {100: 1, 50: 1, 20: 1, 10: 1, 2: 1, 1: 1, 0.25: 1, 0.1: 1, 0.05: 1, 0.01: 4}
        self.assertEqual(expected, cash_money(test_cad))
