
from linkedlist import LinkedList, Node


def find_intersection(l1, l2):
    n1 = l1.head
    n2 = l2.head
    if n1 == None or n2 == None:
        return False

    while True:
        if n1 is n2:
            return n1

        # leave here if they have no intersection (reach the end at the same time)
        if n1.next == None and n2.next==None:
            return None

        n1 = n1.next if n1.next != None else l2.head
        n2 = n2.next if n2.next != None else l1.head


def test_func():
    assert None == find_intersection(LinkedList([1,2,3,4,5]), LinkedList([2,2,3,4,5]))

    # craft 2 intersected lists
    l1 = LinkedList([1,2,3,4,5,6])
    l2 = LinkedList([1,2,3,4,5,6,7,8,9,10])
    node1 = l1.find(6)
    node2 = l2.find(7)
    node1.next = node2
    assert node2 is find_intersection(l1, l2)
