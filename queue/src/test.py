import unittest

from queue import Queue


class QueueTest(unittest.TestCase):

    def setUp(self):
        self.emptyQueue = Queue()

        queue = Queue()
        queue.put(1)
        queue.put(2)
        self.filledQueue = queue

        queue = Queue(size=2)
        queue.put(1)
        queue.put(2)
        self.fullQueue = queue

    def test_is_empty(self):
        self.assertEqual(self.emptyQueue.is_empty(), True)
        self.assertEqual(self.filledQueue.is_empty(), False)
        self.assertEqual(self.fullQueue.is_empty(), False)

    def test_is_full(self):
        self.assertEqual(self.emptyQueue.is_full(), False)
        self.assertEqual(self.filledQueue.is_full(), False)
        self.assertEqual(self.fullQueue.is_full(), True)

    def test_put(self):
        queue = Queue(size=2)
        self.assertEqual(str(queue), '[]')
        queue.put(1)
        self.assertEqual(str(queue), '[1]')
        queue.put(2)
        self.assertEqual(str(queue), '[1, 2]')
        with self.assertRaises(ValueError):
            queue.put(3)

    def test_get(self):
        queue = self.filledQueue
        self.assertEqual(queue.get(), 1)
        self.assertEqual(queue.get(), 2)
        with self.assertRaises(ValueError):
            queue.get()
