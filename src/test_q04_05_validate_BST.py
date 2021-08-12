from tree import TreeNode

def is_valid_bst(root):
    def is_valid(node, low, high):
        if node == None:
            return True
        if node.val < low or node.val > high:
            return False
        valid_l = is_valid(node.left, low, node.val)
        valid_r = is_valid(node.right, node.val, high)
        return True if valid_l and valid_r else False
    return is_valid(root, -99999, 99999)

def test_func():
    N = None
    root = TreeNode.create_tree([8,3,1,N,N,6,4,N,N,7,N,N,10,N,14,13,N,N,N])
    assert True == is_valid_bst(root)
    root = TreeNode.create_tree([8,3,1,N,N,6,2,N,N,7,N,N,10,N,14,13,N,N,N])
    assert False == is_valid_bst(root)
