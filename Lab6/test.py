import unittest
from wchain import find_max_wchain


class TestWchain (unittest.TestCase):
    def setUp(self):
        self.test_vocabulary_1 = ["abab", "ababa", "bab", "b", "ba", "bbbba"]
        self.test_vocabulary_2 = ["sour", "soup", "our", "ou", "tour", "u"]
        self.test_vocabulary_3 = [
            "cell", "cella", "cellar", " cello", "chello"]

    def test_maxwchain_1(self):
        self.assertEqual(find_max_wchain(self.test_vocabulary_1), 5)

    def test_maxwchain_2(self):
        self.assertEqual(find_max_wchain(self.test_vocabulary_2), 4)

    def test_maxwchain_3(self):
        self.assertEqual(find_max_wchain(self.test_vocabulary_3), 3)
