
from linkedlist import LinkedList, Node

'''
[start from dummy head]
round 1 slow=0, fast=1
round 2 slow=1, fast=3
round 3 slow=2, fast=5
round 3 slow=3, fast=7
round 4 slow=4, fast=9

slow stop at 0th while the list has 0-1 nodes
slow stop at 1th while the list has 2-3 nodes
slow stop at 2th while the list has 4-5 nodes
'''

# Solution1: Reverse half of list and compare
# def is_palindrome(l):
#     if l.head == None:
#         return True

#     node = Node(0, l.head)
#     fast = slow = node

#     # step1: find half
#     while True:
#         slow = slow.next

#         if fast.next == None:
#             break
#         fast = fast.next
#         if fast.next == None:
#             break
#         fast = fast.next
#     print(f'slow node = {slow.data}')

#     #step2: reverse list
#     cur = slow
#     prev = None
#     while cur != None:
#         next = cur.next
#         cur.next = prev
#         # forward
#         prev = cur
#         cur = next
#     print(f'head node of rev_list = {prev.data}')

#     #step3: compare two lists
#     rev_node = prev
#     node = l.head
#     while rev_node != node and rev_node != None:  # rev_list will be shorter.
#         if rev_node.data != node.data:
#             return False
#         rev_node = rev_node.next
#         node = node.next

#     return True


# Solution2 : recursively compare  2 (1 (9) 1) 2
def is_palindrome(l):
    def helper(node, length):
        if length == 0:
            return True, node
        if length == 1:
            return True, node.next
        res, cmp = helper(node.next, length - 2)
        if res == False:
            return False, None
        return cmp.data == node.data, cmp.next

    if l.head == None:
        return True
    result, _ = helper(l.head, len(l))
    return result


def test_func():
    assert True == is_palindrome(LinkedList([9]))
    assert True == is_palindrome(LinkedList([2,1,9,1,2]))
    assert True == is_palindrome(LinkedList([2,1,9,9,1,2]))
    assert False == is_palindrome(LinkedList([1,3,4,5,6]))
