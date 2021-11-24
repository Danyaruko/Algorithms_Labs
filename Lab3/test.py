import unittest
from farm import solve_farm


class TestFarm(unittest.TestCase):
    def setUp(self):
        self.cows_number_1 = 8
        self.aggressive_cows_number_1 = 4
        self.stables_1 = [1, 2, 3, 5, 6, 8, 9, 10]

        self.cows_number_2 = 5
        self.aggressive_cows_number_2 = 3
        self.stables_2 = [1, 2, 8, 4, 9]

        self.cows_number_3 = 6
        self.aggressive_cows_number_3 = 3
        self.stables_3 = [1, 2, 7, 5, 11, 12]

    def test_1(self):
        self.assertEqual(solve_farm(self.cows_number_1,
                         self.aggressive_cows_number_1, self.stables_1), 2)

    def test_2(self):
        self.assertEqual(solve_farm(self.cows_number_2,
                         self.aggressive_cows_number_2, self.stables_2), 3)

    def test_3(self):
        self.assertEqual(solve_farm(self.cows_number_3,
                         self.aggressive_cows_number_3, self.stables_3), 5)
