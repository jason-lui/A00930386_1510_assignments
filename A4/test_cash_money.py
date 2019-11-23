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

    def test_cash_money_99_09(self):
        test_cad = 99.09
        expected = {0.01: 4, 0.05: 1, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_19(self):
        test_cad = 99.19
        expected = {0.01: 4, 0.05: 1, 0.1: 1, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_29(self):
        test_cad = 99.29
        expected = {0.01: 4, 0.25: 1, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_39(self):
        test_cad = 99.39
        expected = {0.01: 4, 0.1: 1, 0.25: 1, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_49(self):
        test_cad = 99.49
        expected = {0.01: 4, 0.1: 2, 0.25: 1, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_59(self):
        test_cad = 99.59
        expected = {0.01: 4, 0.05: 1, 0.25: 2, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_69(self):
        test_cad = 99.69
        expected = {0.01: 4, 0.05: 1, 0.1: 1, 0.25: 2, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_79(self):
        test_cad = 99.79
        expected = {0.01: 4, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_89(self):
        test_cad = 99.89
        expected = {0.01: 4, 0.1: 1, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_90(self):
        test_cad = 99.90
        expected = {0.05: 1, 0.1: 1, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_91(self):
        test_cad = 99.91
        expected = {0.01: 1, 0.05: 1, 0.1: 1, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_92(self):
        test_cad = 99.92
        expected = {0.01: 2, 0.05: 1, 0.1: 1, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_93(self):
        test_cad = 99.93
        expected = {0.01: 3, 0.05: 1, 0.1: 1, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_94(self):
        test_cad = 99.94
        expected = {0.01: 4, 0.05: 1, 0.1: 1, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_95(self):
        test_cad = 99.95
        expected = {0.1: 2, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_96(self):
        test_cad = 99.96
        expected = {0.01: 1, 0.1: 2, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_97(self):
        test_cad = 99.97
        expected = {0.01: 2, 0.1: 2, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_98(self):
        test_cad = 99.98
        expected = {0.01: 3, 0.1: 2, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_99_99(self):
        test_cad = 99.99
        expected = {0.01: 4, 0.1: 2, 0.25: 3, 2: 2, 5: 1, 20: 2, 50: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_100_00(self):
        test_cad = 100.00
        expected = {100: 1}
        self.assertEqual(expected, cash_money(test_cad))

    def test_cash_money_183_59(self):
        test_cad = 183.59
        expected = {0.01: 4, 0.05: 1, 0.25: 2, 1: 1, 2: 1, 10: 1, 20: 1, 50: 1, 100: 1}
        self.assertEqual(expected, cash_money(test_cad))
