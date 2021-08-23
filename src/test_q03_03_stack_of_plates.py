#solution1: leave it unfulled after pop_at()
# from stack import Stack

# class SetOfStacks():
#     def __init__(self, single_cap):
#         self._single_cap = single_cap
#         self._stacks = []

#     def is_empty(self):
#         return len(self._stacks) == 0

#     def peek(self):
#         if self.is_empty():
#             return None
#         return self._stacks[-1].peek()

#     def push(self, data):
#         if self.is_empty() or self._stacks[-1].is_full():
#             self._stacks.append(Stack(self._single_cap))
#         self._stacks[-1].push(data)

#     def pop(self):
#         if self.is_empty():
#             return
#         ret = self._stacks[-1].pop()
#         self._del_empty_stacks()
#         return ret

#     def pop_at(self, i):
#         if self.is_empty():
#             return None
#         if i < 0 or i >= len(self._stacks):
#             raise IndexError(f'invalid index {i}, acceptable range= 0-{len(self._stacks)-1}')

#         ret = self._stacks[i].pop()
#         self._del_empty_stacks()
#         return ret

#     def _del_empty_stacks(self):
#         while not self.is_empty() and self._stacks[-1].is_empty():
#             self._stacks.pop()

#     def _dump_stacks(self):
#         print('dump stacks.....:')
#         for i, s in enumerate(self._stacks):
#             print(f'idx{i}= {s}')

# def test_func_stack1():
#     # test case: normal push/pop
#     stk = SetOfStacks(3)
#     data = [1,2,3,4,5,6,7,8,9]
#     for d in data:
#         stk.push(d)

#     for i in range(len(data)-1, -1, -1):
#         assert data[i] == stk.pop()

#     # test case: popAt
#     stk = SetOfStacks(3)
#     data = [1,2,3,4,5,6,7,8,9]
#     for d in data:
#         stk.push(d)

#     assert stk.pop_at(0)==3
#     assert stk.pop_at(1)==6
#     assert stk.pop_at(2)==9
#     assert stk.pop_at(1)==5
#     assert stk.pop_at(1)==4
#     data = [1,2,7,8]
#     for i in range(len(data)-1, -1, -1):
#         assert data[i] == stk.pop()


#################################################
#solution2: shift one element of the whole behind stacks after pop_at.
#           Need to use double linked-list here
class Node2():
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Stack2():
    def __init__(self, cap=None):
        self._front = None
        self._back = None
        self.cap = cap
        self.len = 0

    def is_empty(self):
        return self.len == 0

    def is_full(self):
        return self.len == self.cap if self.cap != None else False

    def peek(self):
        return None if self.is_empty() else self._back.val

    def peek_left(self):
        return None if self.is_empty() else self._front.val

    def push(self, val):
        if self.is_full():
            return

        node = Node2(val, self._back, None)
        if self.is_empty():
            self._front = self._back = node
        else:
            self._back.next = node
            self._back = node
        self.len += 1

    def push_left(self, val):
        if self.is_full():
            return

        node = Node2(val, None, self._front)
        if self.is_empty():
            self._front = self._back = node
        else:
            self._front.prev = node
            self._front = node
        self.len += 1

    def pop(self):
        if self.is_empty():
            return None

        node = self._back
        self.len -= 1
        if self.is_empty():
            self._front = self._back = None
        else:
            self._back.prev.next = None
            self._back = self._back.prev
        return node.val


    def pop_left(self):
        if self.is_empty():
            return None

        node = self._front
        self.len -= 1
        if self.is_empty():
            self._front = self._back = None
        else:
            self._front.next.prev = None
            self._front = self._front.next
        return node.val

    def dump(self):
        out = []
        node = self._front
        while(node != None):
            out += f'{node.val} -> '
            node = node.next
        out += '\n'
        return ''.join(out)

def test_stack2():
    stk = Stack2()
    data = [1,2,3,4,5,6,7,8,9]

    # case: orinary push/pop
    for d in data:
        stk.push(d)
    for i in range(len(data)-1, -1, -1):
        assert data[i] == stk.pop()

    # case: push_left / pop : ordinary queue behavior
    for d in data:
        stk.push_left(d)
    for d in data:
        assert d == stk.pop()

    # case: push() / pop_left : ordinary queue behavior
    for d in data:
        stk.push(d)
    for d in data:
        assert d == stk.pop_left()

    # case: push_left/pop_left : stack behavior still
    for d in data:
        stk.push_left(d)
    for i in range(len(data)-1, -1, -1):
        assert data[i] == stk.pop_left()

class SetOfStacks():
    def __init__(self, single_cap):
        self._single_cap = single_cap
        self._stacks = []

    def is_empty(self):
        return len(self._stacks) == 0

    def push(self, val):
        if self.is_empty() or self._stacks[-1].is_full():
            self._stacks.append(Stack2(self._single_cap))
        self._stacks[-1].push(val)

    def peek(self):
        if self.is_empty():
            return None

        return self._stacks[-1].peek()

    def pop(self):
        if self.is_empty():
            return None

        ret = self._stacks[-1].pop()
        self._del_empty_stack()
        return ret

    def pop_at(self, index):
        if self.is_empty() or 0 > index >= len(self._stacks):
            return None

        ret = self._stacks[index].pop()
        for i in range(index, len(self._stacks)-1):
            self._stacks[i].push(self._stacks[i+1].pop_left())
        self._del_empty_stack()
        return ret

    def _del_empty_stack(self):
        if not self.is_empty() and self._stacks[-1].is_empty():
            self._stacks.pop()

    def _dump_stacks(self):
        print('dump stacks.....:')
        for i, s in enumerate(self._stacks):
            print(f'idx{i}= {s.dump()}')

def test_func_stack2():
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
    assert stk.pop_at(1)==7
    assert stk.pop_at(2)==9
    assert stk.pop_at(1)==8
    assert stk.pop_at(1)==6
    data = [1,2,4,5]
    for i in range(len(data)-1, -1, -1):
        assert data[i] == stk.pop()

