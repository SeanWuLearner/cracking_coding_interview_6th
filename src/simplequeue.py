from linkedlist import Node

class Queue():
    def __init__(self):
        self._front = self._rear = None

    def add(self, data):
        node = Node(data)
        if self._rear == None:
            self._rear = node
            if self._front == None:
                self._front = node
        else:
            self._rear.next = node
            self._rear = self._rear.next

    def remove(self):
        if self.is_empty():
            return None
        node = self._front
        self._front = self._front.next
        if self._front==None:
            self._rear = None
        return node.data

    def peek(self):
        return self._front.data if not self.is_empty() else None

    def is_empty(self):
        return self._front==None or self._rear==None


def test_func():
    q = Queue()

    assert None == q.peek()
    assert None == q.remove()
    assert True == q.is_empty()

    data = [1,2,3,4]
    for i in data:
        q.add(i)

    assert data[0] == q.peek()
    assert False == q.is_empty()

    for i in data:
        assert i == q.remove()

    assert None == q.peek()
    assert None == q.remove()
    assert True == q.is_empty()
