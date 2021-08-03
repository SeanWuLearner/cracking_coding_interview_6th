
class Stack():
    def __init__(self, capacity=None):
        self._buf = []
        self._cap = capacity

    def push(self, data):
        if self.is_full():
            return
        self._buf.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self._buf.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._buf[-1]

    def is_empty(self):
        return len(self._buf) == 0

    def is_full(self):
        return len(self._buf) == self._cap
