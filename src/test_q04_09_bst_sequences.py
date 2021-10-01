from tree import TreeNode

### Solution by me: same approach as book's
# def weave_seq(s1, i1, s2, i2, acc, i3, ret):
#     if i3 == len(s1) + len(s2):
#         ret += [list(acc)]
#         return
#     if i1 < len(s1):
#         acc[i3] = s1[i1]
#         weave_seq(s1, i1+1, s2, i2, acc, i3+1, ret)
#     if i2 < len(s2):
#         acc[i3] = s2[i2]
#         weave_seq(s1, i1, s2, i2+1, acc, i3+1, ret)

# def weave_seqs(seqs1, seqs2):
#     if seqs1 == None and seqs2 == None:
#         return []
#     if seqs1 == None:
#         return seqs2
#     if seqs2 == None:
#         return seqs1
#     ret = []
#     for s1 in seqs1:
#         for s2 in seqs2:
#             acc = [None] * (len(s1) + len(s2))
#             weave_seq(s1, 0, s2, 0, acc, 0, ret)
#     return ret

# def bst_sequences(root):
#     if root == None:
#         return None
#     l = bst_sequences(root.left)
#     r = bst_sequences(root.right)
#     weaved = weave_seqs(l, r)
#     if len(weaved) == 0:
#         weaved += [[root.val]]
#     else:
#         for w in weaved:
#             w.insert(0, root.val)
#     return weaved

### Solution in the book, more compacted and precise API implementation using 
#   list<deque<int>>
from collections import deque

def weave(q1, q2, results, prefix):
    if len(q1) == 0 or len(q2) == 0:
        result = deque(prefix)
        result += q1
        result += q2
        results += [deque(result)]
        return
    # recursive the head of q1 first
    prefix.append(q1.popleft())
    weave(q1,q2, results, prefix)
    q1.appendleft(prefix.pop())

    # recursive the head of q2 first
    prefix.append(q2.popleft())
    weave(q1,q2, results, prefix)
    q2.appendleft(prefix.pop())

def bst_sequences(root):
    if root == None:
        return [deque()]
    results = []
    prefix = deque([root.val])
    l = bst_sequences(root.left)
    r = bst_sequences(root.right)
    for i in l:
        for j in r:
            result = []
            weave(i, j, result, prefix)
            results += result
    return results

def to_2d_list(list_deque_data):
    '''convert a list of deque to a 2D list'''
    ret = []
    for q in list_deque_data:
        ret += [list(q)]
    return ret

def equals(seqs1, seqs2):
    '''compare two 2D lists if they have same lists set regardless of the order'''
    if len(seqs1)!=0 and isinstance(seqs1[0], deque):
        seqs1 = to_2d_list(seqs1)
    if len(seqs2)!=0 and isinstance(seqs2[0], deque):
        seqs2 = to_2d_list(seqs2)
    return sorted(seqs1) == sorted(seqs2)

def test_weave():
    res = []
    q1 = deque([1,2])
    q2 = deque([3,4])
    weave(q1, q2, res, deque())
    assert True==equals(res, [
        [1,2,3,4],
        [1,3,2,4],
        [1,3,4,2],
        [3,1,4,2],
        [3,4,1,2],
        [3,1,2,4]
    ])

def test_func():
    N = None
    tree = TreeNode.create_tree([2,1,N,N,3,N,N])
    assert True == equals(bst_sequences(tree), [[2,3,1],[2,1,3]])

    tree = TreeNode.create_tree([2,1,N,N,3,N,4,N,N])
    ans = [
        [2,3,4,1],
        [2,3,1,4],
        [2,1,3,4]
    ]
    assert True == equals(bst_sequences(tree), ans)
