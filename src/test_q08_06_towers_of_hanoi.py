from stack import Stack
import pytest

class Tower():
    INDEX = {'left':0, 'middle':1, 'right':2}

    def __init__(self, n):
        self._stacks = [Stack(), Stack(), Stack()]
        self.num = n
        for i in range(n, 0, -1):
            self.left.push(i)

    def _index(self, name):
        return self.INDEX.get(name, None)

    @property
    def left(self):
        return self._stacks[self._index('left')]

    @property
    def middle(self):
        return self._stacks[self._index('middle')]

    @property
    def right(self):
        return self._stacks[self._index('right')]

    def _is_move_valid(self, stk_from, stk_to):
        if stk_from.is_empty():
            return False
        if stk_to.is_empty():
            return True
        return stk_to.peek() > stk_from.peek()

    def move(self, pole_from, pole_to):
        stk_from = getattr(self, pole_from)
        stk_to = getattr(self, pole_to)
        if not self._is_move_valid(stk_from, stk_to):
            raise Exception(f'Move from {pole_from}(top={stk_from.peek()}) '
                            f'to {pole_to}(top={stk_to.peek()}) not valid')
        stk_to.push(stk_from.pop())

    def is_win(self):
        # only either middle or right pole has plates.
        if not self.left.is_empty():
            return False

        if self.right.is_empty() and self.middle.is_empty():
            return False

        if (not self.right.is_empty()) and (not self.middle.is_empty()):
            return False

        # the plates on that pole are exactly whole and in order.
        ret = True
        chk_stk = self.right if self.middle.is_empty() else self.middle
        tmp = Stack()
        for i in range(1, self.num + 1):
            val = chk_stk.pop()
            if val != i:
                ret = False
                break
            tmp.push(val)

        while not tmp.is_empty():
            chk_stk.push(tmp.pop())

        return ret

    def __str__(self):
        out = []
        out += f'left = {self.left}'
        out += f'middle = {self.middle}'
        out += f'right = {self.right}'
        return ''.join(out)

def test_tower():
    tower = Tower(2)
    assert False == tower.is_win()
    # NG case: move empty pole
    with pytest.raises(Exception):
        tower.move('right', 'left')
    # OK case: legal move
    tower.move('left', 'middle')
    # NG case: try to move bigger plate on top of smaller one.
    assert False == tower.is_win()
    with pytest.raises(Exception):
        tower.move('left', 'middle')
    tower.move('left', 'right')
    assert False == tower.is_win()
    tower.move('middle', 'right')
    assert True == tower.is_win()


def solve_tower_of_hanoi(tower):
    def move(pole_from, pole_to, pole_inter, n):
        if n<=0 :
            return
        if n==1 :
            tower.move(pole_from, pole_to)
            return
        move(pole_from, pole_inter, pole_to, n-1)
        move(pole_from, pole_to, pole_inter, 1)
        move(pole_inter, pole_to, pole_from, n-1)
    move('left', 'right', 'middle', tower.num)

def test_func():
    tower = Tower(2)
    solve_tower_of_hanoi(tower)
    assert True == tower.is_win()

    tower = Tower(9)
    solve_tower_of_hanoi(tower)
    assert True == tower.is_win()

########################################################
# solution just output string, don't know how to test it...

from functools import wraps

def cached(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        nonlocal cache
        if args in cache:
            print(f'cache hit! {args}')
            return cache[args]
        cache[args] = func(*args)
        return cache[args]
    return wrapper

def tower_of_hanoi_str(n):
    @cached
    def move(from_rod, to_rod, aux_rod, size):
        if size==1:
            return f'move 1 from {from_rod} to {to_rod}\n'
        out = []
        out += move(from_rod, aux_rod, to_rod, size-1)
        out += f'move {size} from {from_rod} to {to_rod}\n'
        out += move(aux_rod, to_rod, from_rod, size-1)
        return out
    out = move('A', 'C', 'B', n)
    return ''.join(out)

if __name__ == "__main__":
    print(tower_of_hanoi_str(5))
