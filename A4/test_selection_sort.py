from unittest import TestCase
from question_4 import selection_sort


class TestSelection_sort(TestCase):

    def test_selection_sort_ValueError(self):
        test_list = []
        expected = ValueError
        self.assertRaises(expected, selection_sort, test_list)

    def test_selection_sort_TypeError_list(self):
        test_list = [False, True, [2, 3]]
        expected = TypeError
        self.assertRaises(expected, selection_sort, test_list)

    def test_selection_sort_TypeError_comparing_str_int(self):
        test_list = ["STR", 2]
        expected = TypeError
        self.assertRaises(expected, selection_sort, test_list)

    def test_selection_sort_TypeError_comparing_str_bool(self):
        test_list = ["STR", True]
        expected = TypeError
        self.assertRaises(expected, selection_sort, test_list)

    def test_selection_sort_TypeError_comparing_str_float(self):
        test_list = ["STR", 2.2]
        expected = TypeError
        self.assertRaises(expected, selection_sort, test_list)

    def test_selection_sort_1_element(self):
        test_list = [0]
        expected = [0]
        self.assertEqual(expected, selection_sort(test_list))

    def test_selection_sort_integers(self):
        test_list = [3, 1, 2, 0]
        expected = [0, 1, 2, 3]
        self.assertEqual(expected, selection_sort(test_list))

    def test_selection_sort_strings(self):
        test_list = ['bae', 'Bae', 'xX', 'bAe']
        expected = ['Bae', 'bAe', 'bae', 'xX']
        self.assertEqual(expected, selection_sort(test_list))

    def test_selection_sort_floats(self):
        test_list = [3.3, 1.1, 2.2]
        expected = [1.1, 2.2, 3.3]
        self.assertEqual(expected, selection_sort(test_list))

    def test_selection_sort_booleans(self):
        test_list = [False, True, False]
        expected = [False, False, True]
        self.assertEqual(expected, selection_sort(test_list))

    def test_selection_sort_mixed(self):
        test_list = [3, 2.2, True]
        expected = [True, 2.2, 3]
        self.assertEqual(expected, selection_sort(test_list))
