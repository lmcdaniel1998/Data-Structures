import unittest
from lab1 import *
# A few test cases.  Add more!!!


class TestLab1(unittest.TestCase):

    def test_max_list_iter_0(self):
        """test NoneType"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_1(self):
        """test empty list"""
        tlist = []
        my_none = None
        self.assertEqual(max_list_iter(tlist), my_none)

    def test_max_list_iter_2(self):
        """test list len 1"""
        tlist = [5]
        my_none = 5
        self.assertEqual(max_list_iter(tlist), my_none)

    def test_max_list_iter_3(self):
        """test average list"""
        tlist = [1, 2, 10, 4, 5, 6]
        my_none = 10
        self.assertEqual(max_list_iter(tlist), my_none)

    def test_max_list_recursive_4(self):
        tlist = [15, 3, 4, 2, 1]
        my_none = 15
        self.assertEqual(max_list_iter(tlist), my_none)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])

    def test_reverse_rec_0(self):
        """test NoneType"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec_1(self):
        """test empty list"""
        initial_list = []
        output_list = None
        self.assertEqual(reverse_rec(initial_list), output_list)

    def test_reverse_rec_2(self):
        """test list len 1"""
        initial_list = [4]
        output_list = [4]
        self.assertEqual(reverse_rec(initial_list), output_list)

    def test_reverse_rec_3(self):
        """test average list"""
        initial_list = [3, 2, 1]
        output_list = [1, 2, 3]
        self.assertEqual(reverse_rec(output_list), initial_list)

    def test_reverse_rec_4(self):
        """test long list"""
        initial_list = [8, 7, 6, 5, 4, 3, 2, 1]
        output_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(reverse_rec(output_list), initial_list)

    def test_bin_search_0(self):
        """test NoneType"""
        tlist = None
        low = 0
        high = 4
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(5, low, high, tlist)

    def test_bin_search_1(self):
        """test empty list"""
        list_val = []
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), None)
        
    def test_bin_search_2(self):
        """provided test"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)

    def test_bin_search_3(self):
        """max at final value"""
        list_val = [1, 2, 3, 4, 5, 6, 7]
        low = 1
        high = 6
        self.assertEqual(bin_search(7, low, high, list_val), 6)

    def test_bin_search_4(self):
        """max at initial value"""
        list_val = [1, 2, 3, 4, 5, 6, 7]
        low = 1
        high = 6
        self.assertEqual(bin_search(2, low, high, list_val), 1)

    def test_bin_search_5(self):
        """test low high same value not present"""
        list_val = [1, 2, 3, 4, 5, 6, 7]
        low = 2
        high = 2
        self.assertEqual(bin_search(4, low, high, list_val), None)

    def test_bin_search_6(self):
        """test low high same value present"""
        list_val = [1, 2, 3, 4, 5, 6, 7]
        low = 2
        high = 2
        self.assertEqual(bin_search(3, low, high, list_val), 2)

    def test_bin_search_7(self):
        """test value not in list"""
        list_val = [1, 2, 3, 4, 5, 6, 7, 8]
        low = 0
        high = 7
        self.assertEqual(bin_search(10, low, high, list_val), None)


if __name__ == "__main__":
        unittest.main()
