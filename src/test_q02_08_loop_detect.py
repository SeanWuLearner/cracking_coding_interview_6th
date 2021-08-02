from linkedlist import LinkedList

def find_loop(l):
    if l.head == None:
        return None

    slow = l.head
    fast = slow.next

    # confirm whether there is a loop first
    while True:
        if fast is slow:
            break

        if fast is None:
            return None
        fast = fast.next
        if fast is None:
            return None
        fast = fast.next
        slow = slow.next

    print(f'meet at {slow.data}')
    return slow
    # find the loop node
    n1 = slow
    n2 = l.head

    while n1 is not n2:
        n1 = n1.next
        n2 = n2.next
    return n1


def test_func():
    assert find_loop(LinkedList([1,2,3,4,5,6,7])) == None

    l = LinkedList([1,2,3,4,5,6,7,8,9,10])
    end_node = l.find(10)
    loop_node = l.find(5)
    end_node.next = loop_node
    assert find_loop(l) == loop_node

    l = LinkedList([1,2,3,4,5,6,7,8,9,10])
    end_node = l.find(10)
    loop_node = l.find(4)
    end_node.next = loop_node
    assert find_loop(l) == loop_node

