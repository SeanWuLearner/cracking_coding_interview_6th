
from linkedlist import LinkedList

def rm_dup(l):
    if l == None:
        return l
    head = l.head
    prev = None
    mem = set()
    while head != None:
        if head.data in mem:
            prev.next = head.next
        else:
            mem.add(head.data)
            prev = head
        head = head.next
    return l


def test_func():
    assert rm_dup(LinkedList([1,2,3,4,5,7])) == LinkedList([1,2,3,4,5,7])
    assert rm_dup(LinkedList([3,3,3,3,3])) == LinkedList([3])
    assert rm_dup(LinkedList([1,2,3,2,5,3,4,7,1])) == LinkedList([1,2,3,5,4,7])
