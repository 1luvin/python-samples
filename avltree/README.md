# AVLTree

An AVL tree (named after inventors Adelson-Velsky and Landis) is a self-balancing binary search tree (BST). In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property. Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases, where *n* is the number of nodes in the tree prior to the operation. Insertions and deletions may require the tree to be rebalanced by one or more tree rotations.

[Read more](https://en.wikipedia.org/wiki/AVL_tree)

## Usage

**Initialize**

```python
tree = AVLTree()
```

**Insert**

```python
tree.insert(10)
tree.insert(20)
```

![Tree](D:\PythonProjects\python-samples\avltree\readme\10_20.png)

**Rotation**

```python
tree.insert(30)
```

![Tree](D:\PythonProjects\python-samples\avltree\readme\10_20_30_br.png)

Since we have an AVL tree, we cannot leave it in this form, because the balance of the tree is disturbed. An AVL tree balance is the difference between the heights of the left and right subtrees. Heights should not differ by more than 1. So if we encounter such a situation, we have to rotate the tree in the appropriate direction. In our case, we have to rotate the tree to the left.

![Tree](D:\PythonProjects\python-samples\avltree\readme\10_20_30.png)

**Other methods**

- insert(value) – inserts new node to the tree

- remove(value) - removes node from the tree

- clear() - removes all nodes from the tree

- contains(value) - checks if node is in the tree

- is_empty() - checks if the tree has no nodes

- get_min_value() - gets a minimum node

- get_max_value() - gets a maximum node

- to_string(order) - a string representation of the tree in the specified order

- print(order) - prints the tree in the specified order

**Orders**

| AVLTree.Order | Output   |
| ------------- | -------- |
| IN            | 10 20 30 |
| PRE           | 20 10 30 |
| POST          | 10 30 20 |
