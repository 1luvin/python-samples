class Queue:
    __EX_EMPTY = 'Queue is empty.'
    __EX_FULL = 'Queue is full.'

    def __init__(self, size: int = 10):
        self.values: list = [None] * size
        self.head: int = 0
        self.tail: int = 0
        self.size: int = size

    def __str__(self) -> str:
        s = '['
        for i in range(self.head, self.tail, 1):
            value = self.values[i]
            if value is not None:
                s += str(value)
            if i + 1 < self.size and self.values[i + 1] is not None:
                s += ', '
        s += ']'
        return s

    def is_empty(self):
        return self.values.count(None) == self.size

    def is_full(self):
        return (self.tail + 1) % (self.size + 1) == self.head

    def put(self, value: object):
        if self.is_full():
            raise ValueError(Queue.__EX_FULL)
        self.values[self.tail] = value
        self.tail = (self.tail + 1) % (self.size + 1)

    def get(self) -> object:
        if self.is_empty():
            raise ValueError(Queue.__EX_EMPTY)
        value = self.values[self.head]
        self.values[self.head] = None
        self.head = (self.head + 1) % self.size
        return value
