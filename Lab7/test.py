import unittest
from kmp_algorithm import kmp_algorithm


class TestKmpAlgorithm(unittest.TestCase):
    def setUp(self):
        self.test_string = "Ubibeneibipatria"
        self.test_substring_1 = "bi"
        self.test_substring_2 = "b"
        self.test_substring_3 = "ibi"

    def test_kmp_algorithm_1(self):
        self.assertListEqual(kmp_algorithm(
            self.test_string, self.test_substring_1), [1, 8])

    def test_kmp_algorithm_2(self):
        self.assertListEqual(kmp_algorithm(
            self.test_string, self.test_substring_2), [1, 3, 8])

    def test_kmp_algorithm_3(self):
        self.assertListEqual(kmp_algorithm(
            self.test_string, self.test_substring_3), [7])
