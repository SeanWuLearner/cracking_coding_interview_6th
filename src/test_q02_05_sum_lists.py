
from linkedlist import LinkedList, Node

def sum(a, b):
    a = a.head
    b = b.head

    head = cur = Node(0)
    carry = 0
    while a != None or b != None:
        a_val = a.data if a!=None else 0
        b_val = b.data if b!=None else 0
        res = a_val + b_val + carry
        carry = int(res / 10)
        cur.next = Node(res % 10)

        cur = cur.next
        a = a.next if a!=None else a
        b = b.next if b!=None else b

    if carry:
        cur.next = Node(carry)

    l = LinkedList([0])
    l.head = head.next
    return l


def test_func():
    assert sum(LinkedList([7,1,6]), LinkedList([7,1,7])) == LinkedList([4,3,3,1])
    assert sum(LinkedList([7]), LinkedList([7,1,7])) == LinkedList([4,2,7])
    assert sum(LinkedList([7,1,7]), LinkedList([7])) == LinkedList([4,2,7])
