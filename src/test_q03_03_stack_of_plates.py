from stack import Stack

class SetOfStacks():
    def __init__(self, single_cap):
        self._single_cap = single_cap
        self._stacks = []

    def is_empty(self):
        return len(self._stacks) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self._stacks[-1].peek()

    def push(self, data):
        if self.is_empty() or self._stacks[-1].is_full():
            self._stacks.append(Stack(self._single_cap))
        self._stacks[-1].push(data)

    def pop(self):
        if self.is_empty():
            return
        ret = self._stacks[-1].pop()
        self._del_empty_stacks()
        return ret

    def pop_at(self, i):
        if self.is_empty():
            return None
        if i < 0 or i >= len(self._stacks):
            raise IndexError(f'invalid index {i}, acceptable range= 0-{len(self._stacks)-1}')

        ret = self._stacks[i].pop()
        self._del_empty_stacks()
        return ret

    def _del_empty_stacks(self):
        while not self.is_empty() and self._stacks[-1].is_empty():
            self._stacks.pop()

    def _dump_stacks(self):
        print('dump stacks.....:')
        for i, s in enumerate(self._stacks):
            print(f'idx{i}= {s}')


def test_func():
    # test case: normal push/pop
    stk = SetOfStacks(3)
    data = [1,2,3,4,5,6,7,8,9]
    for d in data:
        stk.push(d)

    for i in range(len(data)-1, -1, -1):
        assert data[i] == stk.pop()

    # test case: popAt
    stk = SetOfStacks(3)
    data = [1,2,3,4,5,6,7,8,9]
    for d in data:
        stk.push(d)

    assert stk.pop_at(0)==3
    assert stk.pop_at(1)==6
    assert stk.pop_at(2)==9
    assert stk.pop_at(1)==5
    assert stk.pop_at(1)==4
    data = [1,2,7,8]
    for i in range(len(data)-1, -1, -1):
        assert data[i] == stk.pop()
