from tree import TreeNode

def weave_seq(s1, i1, s2, i2, acc, i3, ret):
    if i3 == len(s1) + len(s2):
        ret += [list(acc)]
        return
    if i1 < len(s1):
        acc[i3] = s1[i1]
        weave_seq(s1, i1+1, s2, i2, acc, i3+1, ret)
    if i2 < len(s2):
        acc[i3] = s2[i2]
        weave_seq(s1, i1, s2, i2+1, acc, i3+1, ret)

def weave_seqs(seqs1, seqs2):
    if seqs1 == None and seqs2 == None:
        return []
    if seqs1 == None:
        return seqs2
    if seqs2 == None:
        return seqs1
    ret = []
    for s1 in seqs1:
        for s2 in seqs2:
            acc = [None] * (len(s1) + len(s2))
            weave_seq(s1, 0, s2, 0, acc, 0, ret)
    return ret

def bst_sequences(root):
    if root == None:
        return None
    l = bst_sequences(root.left)
    r = bst_sequences(root.right)
    weaved = weave_seqs(l, r)
    if len(weaved) == 0:
        weaved += [[root.val]]
    else:
        for w in weaved:
            w.insert(0, root.val)
    return weaved

def equals(seqs1, seqs2):
    return sorted(seqs1) == sorted(seqs2)

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
