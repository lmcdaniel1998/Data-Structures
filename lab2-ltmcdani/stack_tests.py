import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
import stack_array
import stack_linked


class TestLab2(unittest.TestCase):
    def test_simple(self):
        stackS = stack_linked.Stack(5)
        stackS.push(0)
        self.assertFalse(stackS.is_empty())
        self.assertFalse(stackS.is_full())
        self.assertEqual(stackS.size(), 1)

    def test_simple_(self):
        stackT = stack_array.Stack(5)
        stackT.push(0)
        self.assertFalse(stackT.is_empty())
        self.assertFalse(stackT.is_full())
        self.assertEqual(stackT.size(), 1)

    def test_array_is_empty(self):
        stackT = stack_array.Stack(7)
        self.assertTrue(stackT.is_empty())

    def test_array_is_full(self):
        stackT = stack_array.Stack(3)
        stackT.push(1)
        stackT.push(2)
        stackT.push(3)
        self.assertTrue(stackT.is_full())

    def test_array_push_0(self):
        stackT = stack_array.Stack(4)
        stackT.push(3)
        stackT.push(2)
        stackT.push(1)
        self.assertEqual(stackT.items, [3, 2, 1, None])

    def test_array_push_1(self):
        stackT = stack_array.Stack(2)
        stackT.push(0)
        stackT.push(10)
        self.assertRaises(IndexError, lambda: stackT.push(1))

    def test_array_pop_0(self):
        stackT = stack_array.Stack(3)
        stackT.push(2)
        stackT.push(1)
        self.assertEqual(stackT.pop(), 1)

    def test_array_pop_1(self):
        stackT = stack_array.Stack(4)
        self.assertRaises(IndexError, lambda: stackT.pop())

    def test_array_pop_2(self):
        stackT = stack_array.Stack(4)
        stackT.push(4)
        stackT.push(5)
        stackT.push("hello")
        self.assertEqual(stackT.pop(), "hello")
        stackT.push(8)
        self.assertEqual(stackT.pop(), 8)
        self.assertEqual(stackT.pop(), 5)

    def test_array_peek(self):
        stackT = stack_array.Stack(3)
        stackT.push(7)
        stackT.push(3)
        stackT.push(1)
        self.assertEqual(stackT.peek(), 1)

    def test_array_peek_2(self):
        stackT = stack_array.Stack(4)
        stackT.push(4)
        stackT.push(5)
        stackT.push("hello")
        self.assertEqual(stackT.peek(), "hello")
        stackT.pop()
        stackT.push(8)
        self.assertEqual(stackT.peek(), 8)
        stackT.pop()
        self.assertEqual(stackT.peek(), 5)

    def test_array_size(self):
        stackT = stack_array.Stack(6)
        stackT.push(5)
        stackT.push(1)
        stackT.push(3)
        stackT.pop()
        stackT.push(7)
        stackT.push(9)
        self.assertEqual(stackT.size(), 4)

    def test_linked_is_empty(self):
        stackS = stack_linked.Stack(7)
        self.assertTrue(stackS.is_empty())

    def test_linked_is_full(self):
        stackS = stack_linked.Stack(3)
        stackS.push(1)
        stackS.push(2)
        stackS.push(3)
        self.assertTrue(stackS.is_full())

    def test_linked_push_0(self):
        stackS = stack_linked.Stack(4)
        stackS.push(3)
        self.assertEqual(stackS.head.data, 3)
        stackS.push(2)
        self.assertEqual(stackS.head.data, 2)
        stackS.push(1)
        self.assertEqual(stackS.head.data, 1)

    def test_linked_push_1(self):
        stackS = stack_linked.Stack(2)
        stackS.push(0)
        stackS.push(10)
        self.assertRaises(IndexError, lambda: stackS.push(1))

    def test_linked_pop_0(self):
        stackS = stack_linked.Stack(3)
        stackS.push(3)
        stackS.push(2)
        self.assertEqual(stackS.pop(), 2)

    def test_linked_pop_1(self):
        stackS = stack_linked.Stack(4)
        self.assertRaises(IndexError, lambda: stackS.pop())

    def test_linked_peek(self):
        stackS = stack_linked.Stack(3)
        stackS.push(3)
        stackS.push(2)
        stackS.push(1)
        self.assertEqual(stackS.peek(), 1)

    def test_linked_size(self):
        stackS = stack_linked.Stack(8)
        stackS.push(3)
        stackS.push(1)
        stackS.pop()
        stackS.push(10)
        stackS.push(21)
        self.assertEqual(stackS.size(), 3)


if __name__ == '__main__': 
    unittest.main()
