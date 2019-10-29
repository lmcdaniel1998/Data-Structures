import unittest
from sorts import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_selection_empty(self):
        nums = []
        sorted_nums = []
        comps = selection_sort(nums)
        # equation for O(n^2) comparisons
        true_comps = ((len(nums) ** 2) - len(nums)) / 2         # 0
        self.assertEqual(comps, true_comps)
        self.assertEqual(nums, sorted_nums)

    def test_selection_worst_case(self):        # there is no worst or best case for selection sort all O(n^2)
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        comps = selection_sort(nums)
        true_comps = ((len(nums) ** 2) - len(nums)) / 2         # 36
        self.assertEqual(comps, true_comps)
        self.assertEqual(nums, sorted_nums)

    def test_selection_best_case(self):
        nums = [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
        sorted_nums = [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
        comps = selection_sort(nums)
        true_comps = ((len(nums) ** 2) - len(nums)) / 2         # 78
        self.assertEqual(comps, true_comps)
        self.assertEqual(nums, sorted_nums)

    def test_selection_large_random(self):          # average case O(n^2)
        random.seed(789)
        nums = random.sample(range(1000), 1000)
        sorted_nums = list(nums)           # create new identical list
        sorted_nums.sort()
        comps = selection_sort(nums)
        true_comps = ((len(nums) ** 2) - len(nums)) / 2         # 499500
        self.assertEqual(comps, true_comps)
        self.assertEqual(nums, sorted_nums)

    def test_insertion_empty(self):
        nums = []
        sorted_nums = []
        comps = insertion_sort(nums)
        true_comps = 0         # 0
        self.assertEqual(comps, true_comps)
        self.assertEqual(nums, sorted_nums)

    def test_insertion_worst_case(self):        # reversed list O(n^2)
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        comps = insertion_sort(nums)
        # equation for O(n^2) comparisons
        true_comps = ((len(nums) ** 2) - len(nums)) / 2         # 36
        self.assertEqual(comps, true_comps)
        self.assertEqual(nums, sorted_nums)

    def test_insertion_best_case(self):         # in order list O(n)
        nums = [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
        sorted_nums = [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
        comps = insertion_sort(nums)
        # equation for O(n) comparisons
        true_comps = (len(nums) - 1)        # 12
        self.assertEqual(comps, true_comps)
        self.assertEqual(nums, sorted_nums)

    def test_insertion_large_random(self):          # random case  around O(n^2)
        random.seed(789)
        nums = random.sample(range(1000), 1000)
        sorted_nums = list(nums)           # create new identical list
        sorted_nums.sort()
        comps = insertion_sort(nums)
        true_comps = 240045      # list specific number but around 1/2 of O(n^2)
        self.assertEqual(comps, true_comps)
        self.assertEqual(nums, sorted_nums)


if __name__ == '__main__': 
    unittest.main()
