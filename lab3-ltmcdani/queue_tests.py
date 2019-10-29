import unittest
import queue_array
import queue_linked


class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = queue_array.Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_linked(self):
        q = queue_linked.Queue(5)
        q.is_empty()
        self.assertFalse(q.is_full())
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.tail.item, 4)
        self.assertEqual(q.head.item, 3)

    def test_linked_is_empty(self):
        q = queue_linked.Queue(3)
        q.enqueue(9)
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_linked_is_full(self):
        q = queue_linked.Queue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertTrue(q.is_full())

    def test_linked_enqueue_1(self):
        q = queue_linked.Queue(2)
        q.enqueue(0)
        q.enqueue(10)
        self.assertRaises(IndexError, lambda: q.enqueue(5))

    def test_linked_enqueue_2(self):
        q = queue_linked.Queue(7)
        q.enqueue(3)
        self.assertEqual(q.tail.item, 3)
        q.enqueue(7)
        self.assertNotEqual(q.tail.item, 3)

    def test_linked_enqueue_3(self):
        q = queue_linked.Queue(4)
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(4)
        q.enqueue(2)
        q.dequeue()
        q.dequeue()
        q.enqueue("hello")
        self.assertEqual(q.tail.item, "hello")

    def test_linked_dequeue_1(self):
        q = queue_linked.Queue(6)
        self.assertRaises(IndexError, lambda: q.dequeue())

    def test_linked_dequeue_2(self):
        q = queue_linked.Queue(3)
        q.enqueue(5)
        q.enqueue(4)
        self.assertEqual(q.dequeue(), 5)

    def test_linked_size(self):
        q = queue_linked.Queue(4)
        q.enqueue(4)
        q.enqueue(2)
        q.enqueue(9)
        q.dequeue()
        q.enqueue(1)
        self.assertEqual(q.size(), 3)

    def test_array_is_empty(self):
        q = queue_array.Queue(2)
        q.enqueue(5)
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_array_is_full(self):
        q = queue_array.Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertTrue(q.is_full())

    def test_array_enqueue_1(self):
        q = queue_array.Queue(2)
        q.enqueue(3)
        q.enqueue("foo")
        self.assertRaises(IndexError, lambda: q.enqueue(5))

    def test_array_enqueue_2(self):
        q = queue_array.Queue(7)
        q.enqueue(3)
        self.assertEqual(q.items[q.front], 3)
        q.enqueue(7)
        self.assertNotEqual(q.items[q.rear], 7)

    def test_array_enqueue_3(self):
        q = queue_array.Queue(4)
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(4)
        q.enqueue(2)
        q.dequeue()
        q.dequeue()
        q.enqueue("hello")
        self.assertEqual(q.items, ["hello", None, 4, 2])

    def test_array_dequeue_1(self):
        q = queue_array.Queue(6)
        self.assertRaises(IndexError, lambda: q.dequeue())

    def test_array_dequeue_2(self):
        q = queue_array.Queue(3)
        q.enqueue(5)
        q.enqueue(4)
        q.enqueue(2)
        q.dequeue()
        q.enqueue(10)
        q.dequeue()
        self.assertEqual(q.dequeue(), 2)

    def test_array_size(self):
        q = queue_array.Queue(5)
        q.enqueue(1)
        q.enqueue(8)
        q.dequeue()
        q.enqueue('glue')
        q.enqueue(12)
        q.enqueue(3)
        q.dequeue()
        q.enqueue(0)
        q.dequeue()
        self.assertEqual(q.size(), 3)


if __name__ == '__main__': 
    unittest.main()
