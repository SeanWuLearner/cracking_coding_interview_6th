
from linkedlist import LinkedList

def kth_to_the_last(l, n):
    head = l.head
    fast = head
    slow = None
    while fast != None:
        fast = fast.next
        if n > 0 :
            n -= 1
        elif n == 0:
            slow = slow.next if slow != None else head
    return slow.data if slow != None else None


def test_func():
    assert kth_to_the_last(LinkedList([1,2,3,4,5,6]), 0) == 6
    assert kth_to_the_last(LinkedList([1,2,3,4,5,6]), 2) == 4
    assert kth_to_the_last(LinkedList([1,2,3,4,5,6]), 6) == None
