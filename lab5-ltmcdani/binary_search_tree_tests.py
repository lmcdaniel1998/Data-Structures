import unittest
from binary_search_tree import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertTrue(bst.delete(10))
        self.assertEqual(bst.tree_height(), None)

    def test_is_empty_01(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())

    def test_is_empty_02(self):
        bst = BinarySearchTree()
        bst.insert(2, "hello")
        self.assertFalse(bst.is_empty())

    def test_search_01(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.search(4))

    def test_search_02(self):
        bst = BinarySearchTree()
        bst.insert(45, 1)
        bst.insert(23, 3)
        bst.insert(34, 2)
        bst.insert(1, 10)
        self.assertTrue(bst.search(34))

    def test_search_03(self):
        bst = BinarySearchTree()
        bst.insert(7, 10)
        bst.insert(1, 2)
        bst.insert(22, 9)
        bst.insert(3, 10)
        self.assertFalse(bst.search(2))

    def test_insert_01(self):
        bst = BinarySearchTree()
        bst.insert(5, "first")
        self.assertEqual(bst.root.data, "first")

    def test_insert_02(self):
        bst = BinarySearchTree()
        bst.insert(8, "first")
        bst.insert(4, "to the left")
        self.assertEqual(bst.root.left.data, "to the left")

    def test_insert_03(self):
        bst = BinarySearchTree()
        bst.insert(15, "first")
        bst.insert(30, "to the right")
        self.assertEqual(bst.root.right.data, "to the right")

    def test_insert_04(self):
        bst = BinarySearchTree()
        bst.insert(11, "alpha")
        bst.insert(4, "beta")
        bst.insert(6, "gamma")
        self.assertEqual(bst.root.left.right.data, "gamma")

    def test_insert_05(self):
        bst = BinarySearchTree()
        bst.insert(4, "h")
        bst.insert(8, "e")
        bst.insert(12, "y")
        bst.insert(1, "z")
        self.assertEqual(bst.root.right.right.key, 12)

    def test_find_min_01(self):
        bst = BinarySearchTree()
        bst.insert(8, 1)
        bst.insert(10, 3)
        bst.insert(7, 2)
        bst.insert(2, 10)
        self.assertEqual(bst.find_min(), (2, 10))

    def test_find_min_02(self):
        bst = BinarySearchTree()
        bst.insert(8, "w")
        bst.insert(15, "x")
        bst.insert(23, "y")
        bst.insert(9, "z")
        self.assertEqual(bst.find_min(), (8, "w"))

    def test_find_max_01(self):
        bst = BinarySearchTree()
        bst.insert(8, 1)
        bst.insert(10, 3)
        bst.insert(7, 2)
        bst.insert(2, 10)
        bst.insert(13, 4)
        bst.insert(1, 45)
        self.assertEqual(bst.find_max(), (13, 4))

    def test_find_max_02(self):
        bst = BinarySearchTree()
        bst.insert(50, "a")
        bst.insert(10, "b")
        bst.insert(7, "c")
        bst.insert(2, "d")
        bst.insert(13, "e")
        bst.insert(1, "f")
        self.assertEqual(bst.find_max(), (50, "a"))

    def test_tree_height_01(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)

    def test_tree_height_02(self):
        bst = BinarySearchTree()
        bst.insert(5, 2)
        bst.insert(3, 1)
        self.assertEqual(bst.tree_height(), 1)

    def test_tree_height_03(self):
        bst = BinarySearchTree()
        bst.insert(10, "a")
        bst.insert(9, "b")
        bst.insert(8, "c")
        bst.insert(7, "d")
        bst.insert(6, "e")
        bst.insert(5, "f")
        bst.insert(4, "g")
        bst.insert(3, "h")
        self.assertEqual(bst.tree_height(), 7)

    def test_tree_height_04(self):
        bst = BinarySearchTree()
        bst.insert(6, "z")
        bst.insert(12, "y")
        bst.insert(3, "x")
        bst.insert(7, "w")
        bst.insert(8, "v")
        bst.insert(2, "u")
        bst.insert(45, "t")
        self.assertEqual(bst.tree_height(), 3)

    def test_preorder_list_01(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder_list(), [])

    def test_preorder_list_02(self):
        bst = BinarySearchTree()
        bst.insert(4, "yellow")
        bst.insert(8, "green")
        bst.insert(12, "blue")
        bst.insert(1, "red")
        self.assertEqual(bst.preorder_list(), [4, 1, 8, 12])

    def test_inorder_list_01(self):
        bst = BinarySearchTree()
        bst.insert(8, 1)
        bst.insert(4, 3)
        bst.insert(12, 6)
        self.assertEqual(bst.inorder_list(), [4, 8, 12])

    def test_inorder_list_02(self):
        bst = BinarySearchTree()
        bst.insert(9, "z")
        bst.insert(5, "a")
        bst.insert(18, "b")
        bst.insert(7, "c")
        bst.insert(20, "d")
        bst.insert(6, "e")
        bst.insert(2, "f")
        bst.insert(13, "g")
        self.assertEqual(bst.inorder_list(), [2, 5, 6, 7, 9, 13, 18, 20])

    def test_inorder_list_03(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.inorder_list(), [])

    def test_delete_01(self):
        bst = BinarySearchTree()
        bst.insert(10, 1)
        bst.insert(4, 2)
        bst.insert(17, 3)
        bst.insert(2, 4)
        bst.insert(7, 5)
        bst.insert(12, 6)
        bst.insert(20, 7)
        bst.insert(18, 8)
        bst.insert(9, 9)
        #bst.delete(17)
        #print(bst.root.right.key)
        self.assertTrue(bst.delete(17))

    def test_delete_02(self):
        bst = BinarySearchTree()
        bst.insert(10, 1)
        bst.insert(4, 2)
        bst.insert(17, 3)
        bst.insert(2, 4)
        bst.insert(7, 5)
        bst.insert(12, 6)
        bst.insert(20, 7)
        bst.insert(18, 8)
        bst.insert(9, 9)
        #bst.delete(2)
        #print(bst.root.left.left)
        self.assertTrue(bst.delete(2))

    def test_delete_03(self):
        bst = BinarySearchTree()
        bst.insert(10, 1)
        bst.insert(4, 2)
        bst.insert(17, 3)
        bst.insert(2, 4)
        bst.insert(7, 5)
        bst.insert(12, 6)
        bst.insert(20, 7)
        bst.insert(18, 8)
        bst.insert(9, 9)
        #bst.delete(7)
        #print(bst.root.left.right.key)
        self.assertTrue(bst.delete(7))

    def test_delete_04(self):
        bst = BinarySearchTree()
        bst.insert(10, 1)
        bst.insert(4, 2)
        bst.insert(17, 3)
        bst.insert(2, 4)
        bst.insert(7, 5)
        bst.insert(12, 6)
        bst.insert(20, 7)
        bst.insert(18, 8)
        bst.insert(9, 9)
        #bst.delete(20)
        #print(bst.root.right.right.key)
        self.assertTrue(bst.delete(20))


if __name__ == '__main__': 
    unittest.main()
