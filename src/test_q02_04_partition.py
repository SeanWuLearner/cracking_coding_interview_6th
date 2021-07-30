
from linkedlist import LinkedList, Node

def partition(l, x):
    node = l.head
    greater = g_now = Node(0)
    less = l_now = Node(0)
    while node is None:
        if node.data >= x:
            g_now.next = node
            g_now = g_now.next
        else:
            l_now.next = node
            l_now = l_now.next
        node = node.next

    l_now.next = greater.next #combine less and greater list together
    l.head = less.next
    return l

def is_partitioned(l, x):
    node = l.head
    greater_now = False
    while node != None:
        if node.data >= x:
            greater_now = True
        else:
            if greater_now:
                return False
        node = node.next
    return True

def test_func():
    # test is_paritioned()
    assert is_partitioned(LinkedList([1,2,3,4,5,6]), 4) == True
    assert is_partitioned(LinkedList([1,2,3,4,5,6]), 1) == True
    assert is_partitioned(LinkedList([1,2,3,4,5,6]), 6) == True
    assert is_partitioned(LinkedList([1,4,3,4,5,6]), 4) == False
    assert is_partitioned(LinkedList([1,4,3,4,5,6]), 5) == True

    # test partition()
    assert is_partitioned(partition(LinkedList([3,5,8,5,10,2,1]), 5), 5) == True
    assert is_partitioned(partition(LinkedList([3,5,8,5,10,2,1]), 8), 8) == True
    assert is_partitioned(partition(LinkedList([3,5,8,5,10,2,1]), 7), 7) == True
    assert is_partitioned(partition(LinkedList([3,5,8,5,10,2,1]), -1), -1) == True
    assert is_partitioned(partition(LinkedList([3,5,8,5,10,2,1]), 11), 11) == True
    assert is_partitioned(partition(LinkedList([3,5,8,5,10,2,1]), 9), 9) == True
