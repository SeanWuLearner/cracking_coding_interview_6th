
from stack import Stack

class MinStack():
    def __init__(self):
        self._stack = Stack()
        self._mins = Stack()

    def is_empty(self):
        return self._stack.is_empty()

    def is_full(self):
        return self._stack.is_full()

    def min(self):
        return self._mins.peek()

    def peek(self):
        return self._stack.peek()

    def push(self, data):
        min = data if self.is_empty() or data < self.min() else self.min()
        self._mins.push(min)
        self._stack.push(data)

    def pop(self):
        self._mins.pop()
        return self._stack.pop()

def test_func():
    stk = MinStack()
    data = [5,3,7,9,1,6]
    min = [5,3,3,3,1,1]
    for i, d in enumerate(data):
        stk.push(d)
        assert min[i] == stk.min()

    for i in range(len(data)-1, -1, -1):
        assert min[i] == stk.min()
        stk.pop()
