from unittest import TestCase
from question_8 import im_not_sleepy


class TestIm_not_sleepy(TestCase):

    def test_im_not_sleepy(self):
        expected = "10:08 uses the most number of bars (21) to represent."
        self.assertEqual(expected, im_not_sleepy())
