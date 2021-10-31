import unittest
from heap_sort import heap_sort
from copy import deepcopy

array_sample = [4, 7, 36, 89, -25, 19, 15]
sorted_in_asc = [-25, 4, 7, 15, 19, 36, 89]
sorted_in_desc = [89, 36, 19, 15, 7, 4, -25]

class TestHeapSort(unittest.TestCase):

    def test_sorting_in_asc(self):
        self.assertListEqual(heap_sort(deepcopy(array_sample), "asc"), sorted_in_asc)

    def test_sorting_in_desc(self):
        self.assertListEqual(heap_sort(deepcopy(array_sample), "desc"), sorted_in_desc)

    def test_sorting_asc_in_asc(self):
        self.assertListEqual(heap_sort(deepcopy(sorted_in_asc), "asc"), sorted_in_asc)

    def test_sorting_asc_in_desc(self):
        self.assertListEqual(heap_sort(deepcopy(sorted_in_asc), "desc"), sorted_in_desc)

    def test_sorting_desc_in_desc(self):
        self.assertListEqual(heap_sort(deepcopy(sorted_in_desc), "desc"), sorted_in_desc)

    def test_sorting_desc_in_asc(self):
        self.assertListEqual(heap_sort(deepcopy(sorted_in_desc), "asc"), sorted_in_asc)