
# Fixed-sized 3 stacks implementation
class ThreeStack():
    NUM_STACKS = 3

    class StackInfo():
        def __init__(self, start, end, idx):
            self.start = start
            self.end = end
            self.idx = idx

        def __str__(self):
            return f'(start={self.start}, end={self.end}, idx={self.idx})'

    def __init__(self, buf):
        self._buf = buf
        self._buflen = len(buf)
        self.alloc_stacks()

    def alloc_stacks(self):
        chunck_size = int(self._buflen / self.NUM_STACKS)
        self._stacks = []
        for i in range(self.NUM_STACKS):
            start = chunck_size * i
            end = chunck_size * (i+1) if i!= self.NUM_STACKS-1 else self._buflen
            self._stacks.append(self.StackInfo(start, end, None))


    def _stack_idx_validate(self, stk_idx):
        if stk_idx < 0 or stk_idx >= self.NUM_STACKS:
            raise IndexError(f'Invalid idx({stk_idx}), only accept 0-{self.NUM_STACKS-1}')

    def push(self, stk_idx, data):
        self._stack_idx_validate(stk_idx)

        if self.is_full(stk_idx):
            raise BufferError(f'Stack{stk_idx} is full, unable to push')

        info = self._stacks[stk_idx]
        info.idx = info.start if info.idx==None else info.idx+1
        self._buf[info.idx] = data
        self.dump_stacks_info()

    def pop(self, stk_idx):
        self._stack_idx_validate(stk_idx)

        if self.is_empty(stk_idx):
            return None
        info = self._stacks[stk_idx]
        ret = self._buf[info.idx]
        info.idx = None if info.idx==info.start else info.idx-1
        return ret

    def peek(self, stk_idx):
        self._stack_idx_validate(stk_idx)
        info = self._stacks[stk_idx]
        return self._buf[info.idx] if info.idx!=None else None

    def is_empty(self, stk_idx):
        self._stack_idx_validate(stk_idx)
        info = self._stacks[stk_idx]
        return True if info.idx==None else False

    def is_full(self, stk_idx):
        self._stack_idx_validate(stk_idx)
        info = self._stacks[stk_idx]
        if info.idx == None:
            return False
        return True if info.idx==info.end-1 else False

    #... debug func ...
    def dump_stacks_info(self):
        print('dump stacks....:')
        for i in range(self.NUM_STACKS):
            print(self._stacks[i])


def test_func():

    buf = [None] * 9
    chunck_size = 3
    stks = ThreeStack(buf)
    for i in range(3):
        assert stks.is_empty(i) == True
        assert stks.is_full(i) == False

    data = 1
    for i in range(3):
        for _ in range(chunck_size):
            stks.push(i, data)
            data += 1

    for i in range(3):
        assert stks.is_empty(i) == False
        assert stks.is_full(i) == True

    assert stks.peek(0)==3
    assert stks.peek(1)==6
    assert stks.peek(2)==9

    data = 9
    for i in range(2, -1, -1):
        for _ in range(chunck_size):
            assert stks.pop(i) == data
            data -= 1

    for i in range(3):
        assert stks.is_empty(i) == True
        assert stks.is_full(i) == False
