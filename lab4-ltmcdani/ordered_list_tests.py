import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    '''def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)'''

    def test_is_empty(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())

    def test_add_01(self):
        t_list = OrderedList()
        t_list.add(5)
        self.assertEqual(t_list.sentinel.next.item, 5)

    def test_add_02(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(1)
        t_list.add(6)
        t_list.add(4)
        self.assertEqual(t_list.sentinel.next.item, 1)

    def test_add_03(self):
        t_list = OrderedList()
        t_list.add(14)
        t_list.add(5)
        self.assertEqual(t_list.sentinel.next.next.item, 14)

    def test_add_04(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(4)
        self.assertEqual(t_list.sentinel.next.next.next, t_list.sentinel)

    def test_add_05(self):
        t_list = OrderedList()
        t_list.add(8)
        t_list.add(1)
        self.assertEqual(t_list.sentinel.next.next.prev.item, 1)

    def test_remove_01(self):
        t_list = OrderedList()
        t_list.add(6)
        self.assertFalse(t_list.remove(7))

    def test_remove_02(self):
        t_list = OrderedList()
        t_list.add(2)
        self.assertTrue(t_list.remove(2))

    def test_remove_03(self):
        t_list = OrderedList()
        t_list.add(3)
        t_list.add(4)
        t_list.add(10)
        t_list.add(45)
        t_list.add(1)
        self.assertTrue(t_list.remove(10))

    def test_index_01(self):
        t_list = OrderedList()
        self.assertEqual(t_list.index(7), None)

    def test_index_02(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.index(10), 0)

    def test_index_03(self):
        t_list = OrderedList()
        t_list.add(12)
        t_list.add(1)
        t_list.add(10)
        self.assertEqual(t_list.index(2), None)

    def test_index_04(self):
        t_list = OrderedList()
        t_list.add(3)
        t_list.add(5)
        t_list.add(10)
        self.assertEqual(t_list.index(5), 1)

    def test_index_05(self):
        t_list = OrderedList()
        t_list.add(8)
        t_list.add(2)
        t_list.add(1)
        t_list.add(4)
        t_list.add(6)
        self.assertEqual(t_list.index(6), 3)

    def test_pop_01(self):
        t_list = OrderedList()
        self.assertRaises(IndexError, lambda: t_list.pop(5))

    def test_pop_02(self):
        t_list = OrderedList()
        t_list.add(5)
        t_list.add(7)
        self.assertRaises(IndexError, lambda: t_list.pop(-1))

    def test_pop_03(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(2)
        t_list.add(12)
        t_list.add(4)
        self.assertRaises(IndexError, lambda: t_list.pop(6))

    def test_pop_04(self):
        t_list = OrderedList()
        t_list.add(5)
        t_list.add(2)
        t_list.add(9)
        self.assertEqual(t_list.pop(0), 2)

    def test_pop_05(self):
        t_list = OrderedList()
        t_list.add(3)
        t_list.add(9)
        t_list.add(8)
        t_list.add(13)
        t_list.add(7)
        print(t_list.python_list())
        self.assertEqual(t_list.pop(2), 8)

    def test_search_01(self):
        t_list = OrderedList()
        self.assertFalse(t_list.search(4))

    def test_search_02(self):
        t_list = OrderedList()
        t_list.add(7)
        self.assertTrue(t_list.search(7))

    def test_search_03(self):
        t_list = OrderedList()
        t_list.add(0)
        t_list.add(2)
        self.assertFalse(t_list.search(6))

    def test_search_04(self):
        t_list = OrderedList()
        t_list.add(5)
        t_list.add(1)
        t_list.add(10)
        t_list.add(4)
        t_list.add(8)
        self.assertTrue(t_list.search(4))

    def test_search_05(self):
        t_list = OrderedList()
        t_list.add(5)
        t_list.add(1)
        t_list.add(10)
        t_list.add(4)
        t_list.add(56)
        t_list.add(111)
        t_list.add(3)
        t_list.add(9)
        t_list.add(8)
        self.assertTrue(t_list.search(111))

    def test_search_06(self):
        t_list = OrderedList()
        t_list.add(3)
        t_list.add(5)
        t_list.add(6)
        self.assertTrue(t_list.search(5))

    def test_python_list_01(self):
        t_list = OrderedList()
        t_list.add(8)
        t_list.add(2)
        t_list.add(11)
        t_list.add(6)
        t_list.add(4)
        t_list.add(12)
        self.assertEqual(t_list.python_list(), [2, 4, 6, 8, 11, 12])

    def test_python_list_02(self):
        t_list = OrderedList()
        self.assertRaises(IndexError, lambda: t_list.python_list())

    def test_python_list_03(self):
        t_list = OrderedList()
        t_list.add(3)
        self.assertEqual(t_list.python_list(), [3])

    '''def test_reverse_python_list(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(2)
        t_list.add(3)
        t_list.add(4)
        t_list.add(5)
        t_list.add(6)
        self.assertEqual(t_list.python_list_reversed(), [6, 5, 4, 3, 2, 1])'''

    def test_size_01(self):
        t_list = OrderedList()
        self.assertEqual(t_list.size(), 0)

    def test_size_02(self):
        t_list = OrderedList()
        t_list.add(2)
        t_list.add(6)
        t_list.add(1)
        t_list.add(10)
        self.assertEqual(t_list.size(), 4)


if __name__ == '__main__': 
    unittest.main()
