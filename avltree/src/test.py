import unittest

from avltree import AVLTree


class AVLTreeTest(unittest.TestCase):

    def setUp(self):
        tree = AVLTree()
        self.emptyTree = tree

        tree = AVLTree()
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)
        self.filledTree = tree

    def test_get_min_value(self):
        self.assertEqual(self.filledTree.get_min_value(), 1)
        self.assertNotEqual(self.filledTree.get_min_value(), 3)

    def test_get_max_value(self):
        self.assertEqual(self.filledTree.get_max_value(), 3)
        self.assertNotEqual(self.filledTree.get_max_value(), 1)

    def test_contains(self):
        self.assertEqual(self.filledTree.contains(1), True)
        self.assertEqual(self.filledTree.contains(4), False)

    def test_is_empty(self):
        self.assertEqual(self.emptyTree.is_empty(), True)
        self.assertEqual(self.filledTree.is_empty(), False)

    def test_insert(self):
        tree = AVLTree()
        self.assertEqual(tree.contains(1), False)
        tree.insert(1)
        self.assertEqual(tree.contains(1), True)
        self.assertEqual(tree.contains(2), False)
        tree.insert(2)
        self.assertEqual(tree.contains(2), True)

    def test_remove(self):
        tree = AVLTree()
        tree.insert(1)
        tree.insert(2)
        self.assertEqual(tree.contains(1), True)
        tree.remove(1)
        self.assertEqual(tree.contains(1), False)
        self.assertEqual(tree.contains(2), True)
        tree.remove(2)
        self.assertEqual(tree.contains(2), False)

    def test_clear(self):
        tree = AVLTree()
        tree.insert(1)
        tree.insert(2)
        self.assertEqual(tree.is_empty(), False)
        tree.clear()
        self.assertEqual(tree.is_empty(), True)

    def test_to_string(self):
        self.assertEqual(self.filledTree.to_string(AVLTree.Order.IN), '1 2 3')
        self.assertEqual(self.filledTree.to_string(AVLTree.Order.PRE), '2 1 3')
        self.assertEqual(self.filledTree.to_string(AVLTree.Order.POST), '1 3 2')

    def test_rotate_left(self):
        tree = AVLTree()
        tree.insert(1)
        tree.insert(2)
        self.assertEqual(tree.root.value, 1)
        tree.insert(3)
        self.assertEqual(tree.root.value, 2)
        tree.insert(4)
        self.assertEqual(tree.root.value, 2)
        tree.insert(5)
        self.assertEqual(tree.root.value, 2)

    def test_rotate_right(self):
        tree = AVLTree()
        tree.insert(5)
        tree.insert(4)
        self.assertEqual(tree.root.value, 5)
        tree.insert(3)
        self.assertEqual(tree.root.value, 4)
        tree.insert(2)
        self.assertEqual(tree.root.value, 4)
        tree.insert(1)
        self.assertEqual(tree.root.value, 4)


if __name__ == '__main__':
    unittest.main()
