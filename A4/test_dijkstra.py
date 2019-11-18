from unittest import TestCase
from question_3 import dijkstra


class TestDijkstra(TestCase):

    def test_dijkstra_already_sorted(self):
        sorted_test_list = ['red', 'red', 'red', 'white', 'white', 'white', 'blue', 'blue', 'blue']
        expected = ['red', 'red', 'red', 'white', 'white', 'white', 'blue', 'blue', 'blue']
        dijkstra(sorted_test_list)
        self.assertEqual(expected, sorted_test_list)

    def test_dijkstra_unsorted(self):
        unsorted_test_list = ['red', 'white', 'red', 'blue', 'red', 'white', 'blue', 'white', 'blue']
        expected = ['red', 'red', 'red', 'white', 'white', 'white', 'blue', 'blue', 'blue']
        dijkstra(unsorted_test_list)
        self.assertEqual(expected, unsorted_test_list)
