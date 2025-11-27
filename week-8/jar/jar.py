class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Wrong Input')
        self._size = 0
        self._capacity = capacity

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Negative can't deposit")
        if self._size + n > self._capacity: 
            raise ValueError('Not enough Space')
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Negative number Can't be taken")
        if n > self._size:
            raise ValueError('Not enough size')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size