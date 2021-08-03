from stack import Stack

def move_stack_data(src, dst):
    while not src.is_empty():
        dst.push(src.pop())

class Queue():
    def __init__(self):
        self._buf = Stack()

    def add(self, data):
        self._buf.push(data)

    def remove(self):
        if self._buf.is_empty():
            return None
        tmp = Stack()
        move_stack_data(self._buf, tmp)
        ret = tmp.pop()
        move_stack_data(tmp, self._buf)
        return ret


def test_func():
    q = Queue()

    for d in [1,2,3,4,5]:
        q.add(d)

    for d in [1,2,3]:
        assert d == q.remove()

    for d in [6,7]:
        q.add(d)

    for d in [4,5,6,7]:
        assert d == q.remove()
