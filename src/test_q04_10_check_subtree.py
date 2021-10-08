from tree import TreeNode


# solution1: get their preorder strings, then compare.
# def is_subtree(t1, t2):
#     '''t1 is bigger than t2 by their definitions'''
#     if t1==None and t2==None:
#         return True
#     elif t1==None or t2==None:
#         return False

#     s1 = str(t1)
#     s2 = str(t2)
#     if s2 in s1:
#         return True
#     else:
#         return False

# solution2: recursive one, might be more inefficient.
def is_equal(t1, t2):
    if t1==None and t2==None:
        return True
    if t1==None or t2==None:
        return False
    if t1.val != t2.val:
        return False
    return is_equal(t1.left, t2.left) and is_equal(t1.right, t2.right)

def is_subtree(t1, t2):
    if is_equal(t1, t2)==True:
        return True
    if t1==None: # base case: unable to index t1.left and t1.right.
        return False
    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)


def test_func():
    '''
    1
    ├── 3
    │   ├── 7
    │   └── 6
    └── 2
        ├── 5
        └── 4
    '''
    N = None
    t1 = TreeNode.create_tree([1,2,4,N,N,5,N,N,3,6,N,N,7,N,N])
    t2 = TreeNode.create_tree([3,6,N,N,7,N,N])
    '''
    3
    ├── 7
    └── 6
    '''
    assert True == is_subtree(t1, t2)
    t2 = TreeNode.create_tree([2,4,N,N,5,N,7,N,N])
    '''
    2
    ├── 5
    │   ├── 7
    └── 4
    '''
    assert False == is_subtree(t1, t2)
    t2 = TreeNode.create_tree([2,4,N,N,5,N,N])
    '''
    2
    ├── 5
    └── 4
    '''
    assert True == is_subtree(t1, t2)

    t2 = TreeNode.create_tree([1,2,N,N,3,N,N])
    '''
    1
    ├── 3
    └── 2
    '''
    assert False == is_subtree(t1, t2)

