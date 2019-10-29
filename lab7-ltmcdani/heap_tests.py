import unittest
from heap import *


class TestHeap(unittest.TestCase):

    def test_enqueue_01(self):
        my_heap = MaxHeap(6)
        my_heap.enqueue(20)
        my_heap.enqueue(11)
        my_heap.enqueue(30)
        my_heap.enqueue(5)
        self.assertEqual(my_heap.contents(), [30, 11, 20, 5])

    def test_enqueue_02(self):
        my_heap = MaxHeap(8)
        my_heap.enqueue(12)
        my_heap.enqueue(6)
        my_heap.enqueue(11)
        my_heap.enqueue(22)
        my_heap.enqueue(24)
        self.assertEqual(my_heap.contents(), [24, 22, 11, 6, 12])

    def test_enqueue_03(self):
        my_heap = MaxHeap(5)
        my_heap.enqueue(12)
        my_heap.enqueue(6)
        my_heap.enqueue(11)
        my_heap.enqueue(22)
        my_heap.enqueue(24)
        self.assertFalse(my_heap.enqueue(15))

    def test_dequeue_01(self):
        my_heap = MaxHeap(8)
        my_heap.enqueue(12)
        my_heap.enqueue(6)
        my_heap.enqueue(11)
        my_heap.enqueue(22)
        my_heap.enqueue(24)
        my_heap.dequeue()
        self.assertEqual(my_heap.contents(), [22, 12, 11, 6])

    def test_dequeue_02(self):
        my_heap = MaxHeap(4)
        my_heap.enqueue(6)
        my_heap.enqueue(17)
        my_heap.enqueue(23)
        my_heap.enqueue(45)
        my_heap.dequeue()
        self.assertEqual(my_heap.contents(), [23, 6, 17])
        my_heap.dequeue()
        self.assertEqual(my_heap.contents(), [17, 6])
        my_heap.dequeue()
        self.assertEqual(my_heap.contents(), [6])

    def test_build_heap_01(self):
        test_list = [1, 2, 3, 4, 5]
        proper_order = [5, 4, 3, 1, 2]
        my_heap = MaxHeap(9)
        my_heap.build_heap(test_list)
        self.assertEqual(my_heap.contents(), proper_order)

    def test_01_enqueue(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertTrue(insert)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])

    def test_02_dequeue(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)
        self.assertEqual(test_heap.get_size(), 5)
        self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])

    def test_03_heap_contents(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([1, 2, 3])
        self.assertEqual(test_heap.contents(), [3, 2, 1])

    def test_04_build_heap(self):
        test_heap = MaxHeap(8)
        built = test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertTrue(built)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_05_is_empty(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())

    def test_06_is_full(self):
        test_heap = MaxHeap(5)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())

    def test_07_get_heap_cap(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.capacity(), 7)

    def test_08_get_size(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_size(), 6)

    def test_09_perc_down(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_10_perc_up(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_up(6)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_11_heap_sort_ascending(self):
        test_heap = MaxHeap()
        list1 = [2, 9, 7, 6, 5, 8]
        self.assertEqual(test_heap.heap_sort_ascending(list1), [2, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
