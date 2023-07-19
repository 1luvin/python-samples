class Stack:
    __EX_EMPTY = 'Stack is empty.'
    __EX_FULL = 'Stack is full.'

    def __init__(self, size: int = 10):
        self.values: list = [None] * size
        self.index: int = 0
        self.size: int = size

    def __str__(self) -> str:
        s = '['
        for i in range(self.size):
            value = self.values[i]
            if value is not None:
                s += str(value)
            if i + 1 < self.size and self.values[i + 1] is not None:
                s += ', '
        s += ']'
        return s

    def is_empty(self) -> bool:
        return self.index == 0

    def is_full(self) -> bool:
        return self.index == self.size

    def push(self, value: object):
        if self.is_full():
            raise ValueError(Stack.__EX_FULL)
        self.values[self.index] = value
        self.index += 1

    def pop(self) -> object:
        if self.is_empty():
            raise ValueError(Stack.__EX_EMPTY)
        self.index -= 1
        value = self.values[self.index]
        self.values[self.index] = None
        return value
