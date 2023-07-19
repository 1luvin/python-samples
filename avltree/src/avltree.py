class AVLTree:
    # Public

    class Node:
        def __init__(self, value: object):
            self.value: object = value
            self.left: AVLTree.Node = None
            self.right: AVLTree.Node = None
            self.height: int = 1

    class Order:
        IN = 0
        PRE = 1
        POST = 2

    __EX_EMPTY_TREE = 'Tree is empty.'
    __EX_ORDER_NOT_EXISTS = 'There is no such order. Use one of AVLTree.Order'

    def __init__(self):
        self.root: AVLTree.Node = None

    def get_min_value(self) -> object:
        self.__check_is_empty()

        return self.__get_min_value_node(self.root).value

    def get_max_value(self) -> object:
        self.__check_is_empty()

        return self.__get_max_value_node(self.root).value

    def contains(self, value: object) -> bool:
        return self.__contains(self.root, value)

    def is_empty(self) -> bool:
        return self.root is None

    def insert(self, value: object):
        if self.is_empty():
            self.root = AVLTree.Node(value)

        self.root = self.__insert(self.root, value)

    def remove(self, value: object):
        self.root = self.__remove(self.root, value)

    def clear(self):
        self.root = self.__clear_nodes(self.root)

    def to_string(self, order: Order = Order.IN):
        if order == AVLTree.Order.IN:
            return self.__to_string_in_order(self.root)
        elif order == AVLTree.Order.PRE:
            return self.__to_string_pre_order(self.root)
        elif order == AVLTree.Order.POST:
            return self.__to_string_post_order(self.root)
        else:
            raise ValueError(AVLTree.__EX_ORDER_NOT_EXISTS)

    def print(self, order: Order = Order.IN):
        print(self.to_string(order))

    # Private

    def __height(self, node: Node) -> int:
        if node is None:
            return 0
        return node.height

    def __right_rotate(self, y: Node) -> Node:
        x = y.left
        tmp = x.right
        x.right = y
        y.left = tmp

        y.height = max(self.__height(y.left), self.__height(y.right)) + 1
        x.height = max(self.__height(x.left), self.__height(x.right)) + 1

        return x

    def __left_rotate(self, x: Node) -> Node:
        y = x.right
        tmp = y.left
        y.left = x
        x.right = tmp

        x.height = max(self.__height(x.left), self.__height(x.right)) + 1
        y.height = max(self.__height(y.left), self.__height(y.right)) + 1

        return y

    def __get_balance(self, node: Node) -> int:
        if node is None:
            return 0
        return self.__height(node.left) - self.__height(node.right)

    def __get_min_value_node(self, node: Node) -> Node:
        curr = node
        while curr.left is not None:
            curr = curr.left

        return curr

    def __get_max_value_node(self, node: Node) -> Node:
        curr = node
        while curr.right is not None:
            curr = curr.right

        return curr

    def __contains(self, node: Node, value: object) -> bool:
        while node is not None:
            if node.value == value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right

        return False

    def __insert(self, node: Node, value: object) -> Node:
        if node is None:
            return AVLTree.Node(value)

        if value < node.value:
            node.left = self.__insert(node.left, value)
        elif value > node.value:
            node.right = self.__insert(node.right, value)
        else:
            return node

        node.height = 1 + max(self.__height(node.left), self.__height(node.right))

        balance = self.__get_balance(node)

        if balance > 1 and value < node.left.value:
            return self.__right_rotate(node)

        if balance < -1 and value > node.right.value:
            return self.__left_rotate(node)

        if balance > 1 and value > node.left.value:
            node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)

        if balance < -1 and value < node.right.value:
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)

        return node

    def __remove(self, node: Node, value: object) -> Node:
        if node is None:
            return None

        if value < node.value:
            node.left = self.__remove(node.left, value)
        elif value > node.value:
            node.right = self.__remove(node.right, value)
        elif node.left is None:
            node = node.right
        elif node.right is None:
            node = node.left
        else:
            temp: AVLTree.Node = self.__get_min_value_node(node.right)
            node.value = temp.value
            node.right = self.__remove(node.right, temp.value)

        if node is None:
            return None

        node.height = 1 + max(self.__height(node.left), self.__height(node.right))

        balance = self.__get_balance(node)

        if balance > 1 and self.__get_balance(node.left) >= 0:
            return self.__right_rotate(node)

        if balance > 1 and self.__get_balance(node.left) < 0:
            self.root.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)

        if balance < -1 and self.__get_balance(node.right) <= 0:
            return self.__left_rotate(node)

        if balance < -1 and self.__get_balance(node.right) > 0:
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)

        return node

    def __clear_nodes(self, root: Node) -> Node:
        if root is None:
            return None

        root.left = self.__clear_nodes(root.left)
        root.right = self.__clear_nodes(root.right)

    def __to_string_in_order(self, root: Node) -> str:
        s = ''
        if root is not None:
            if root.left is not None:
                s += f'{self.__to_string_in_order(root.left)} '
            s += str(root.value)
            if root.right is not None:
                s += f' {self.__to_string_in_order(root.right)}'

        return s

    def __to_string_pre_order(self, root: Node):
        s = ''
        if root is not None:
            s += str(root.value)
            if root.left is not None:
                s += f' {self.__to_string_pre_order(root.left)}'
            if root.right is not None:
                s += f' {self.__to_string_pre_order(root.right)}'

        return s

    def __to_string_post_order(self, root: Node):
        s = ''
        if root is not None:
            if root.left is not None:
                s += f'{self.__to_string_post_order(root.left)} '
            if root.right is not None:
                s += f'{self.__to_string_post_order(root.right)} '
            s += str(root.value)

        return s

    def __check_is_empty(self):
        if self.is_empty():
            raise ValueError(AVLTree.__EX_EMPTY_TREE)
