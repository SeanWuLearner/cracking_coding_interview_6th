
from linkedlist import LinkedList

def rm_node(node):
    node.data = node.next.data
    node.next = node.next.next


def test_func():
    l = LinkedList([1,2,3,4,5,6])
    rm_node(l.find(5))
    assert l == LinkedList([1,2,3,4,6])

    l = LinkedList([1,2,3,4,5,6])
    rm_node(l.find(2))
    assert l == LinkedList([1,3,4,5,6])
