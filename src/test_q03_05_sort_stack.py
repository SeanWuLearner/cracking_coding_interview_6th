from stack import Stack

def move_stack_data(src, dst):
    while not src.is_empty():
        dst.push(src.pop())

def sort_stack(s):
    buf = Stack()

    # Put all elements into buf in decreasing order (max on top)
    while not s.is_empty():
        cur = s.pop()
        pop_cnt = 0
        # keep poping buf until its top is less than cur
        while not buf.is_empty() and cur < buf.peek():
            s.push(buf.pop())
            pop_cnt +=1
        # push cur
        buf.push(cur)
        # throw those pops back to buf
        for _ in range(pop_cnt):
            buf.push(s.pop())

    # reverse the result back to s
    move_stack_data(buf, s)
    return s


def test_func():
    s = Stack()
    data = [1,5,3,9,7,3,4,6]
    sorted_data = sorted(data) #[1, 3, 3, 4, 5, 6, 7, 9]
    for d in data:
        s.push(d)

    s = sort_stack(s)
    for d in sorted_data:
        assert d == s.pop()
