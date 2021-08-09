
from linkedlist import LinkedList, Node

# Solution1: idea len(l1 + l2) = len(l2 + l1), they will reach the intersection on 2nd run.
# def find_intersection(l1, l2):
#     n1 = l1.head
#     n2 = l2.head
#     if n1 == None or n2 == None:
#         return False

#     while True:
#         if n1 is n2:
#             return n1

#         # leave here if they have no intersection (reach the end at the same time)
#         if n1.next == None and n2.next==None:
#             return None

#         n1 = n1.next if n1.next != None else l2.head
#         n2 = n2.next if n2.next != None else l1.head


# Solution 2: Figure out len diff on both list in 1st pass. On 2nd pass,
#             elminate the diff to make them arrive the intersection together.
def find_len(node):
    length = 0
    while node != None:
        length += 1
        node = node.next
    return length

def find_intersection(l1, l2):
    n1 = l1.head
    n2 = l2.head

    len1 = find_len(n1)
    len2 = find_len(n2)

    if len1 > len2:
        longer, shorter = n1, n2
    else:
        longer, shorter = n2, n1

    len_diff = abs(len1 - len2)

    # step1: forward longer list with len_diff nodes
    while len_diff != 0:
        longer = longer.next
        len_diff -= 1

    #step2: proceed two list together
    while longer != None or shorter != None:
        if longer is shorter:
            return longer
        longer = longer.next
        shorter = shorter.next
    return None


def test_func():
    assert None == find_intersection(LinkedList([1,2,3,4,5]), LinkedList([2,2,3,4,5]))

    # craft 2 intersected lists
    l1 = LinkedList([1,2,3,4,5,6])
    l2 = LinkedList([1,2,3,4,5,6,7,8,9,10])
    node1 = l1.find(6)
    node2 = l2.find(7)
    node1.next = node2
    assert node2 is find_intersection(l1, l2)
