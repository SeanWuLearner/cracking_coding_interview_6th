from tree import TreeNode

def is_balanced(root):
    height_l = 0 if root.left==None else root.left.height
    height_r = 0 if root.right==None else root.right.height
    return abs(height_l - height_r) < 2

def test_func():
    # case: no level diff
    node = TreeNode.create_tree([1,2,4,None,None,5,None,None,3,6,None,None,7,None,None])
    assert True == is_balanced(node)

    # case: level differ by 1, left subtree longer
    node = TreeNode.create_tree([1,2,4,None,None,5,None,None,3,None,None])
    assert True == is_balanced(node)

    # case: level differ by 1, right subtree longer
    node = TreeNode.create_tree([1,2,None,None,3,6,None,None,7,None,None])
    assert True == is_balanced(node)

    # case: level differ by 2
    node = TreeNode.create_tree([1,2,None,None,3,6,None,None,7, 8,None, None, None])
    assert False == is_balanced(node)

    # case: level differ by 2, no left subtree
    node = TreeNode.create_tree([1,None,3,6,None,None,7,None, None])
    assert False == is_balanced(node)
