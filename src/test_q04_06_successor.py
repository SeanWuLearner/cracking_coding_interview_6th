from tree import TreeNode

def leftmost_at_right(node):
    if node.right == None:
        return None
    cur = node.right
    while cur.left != None:
        cur = cur.left
    return cur

def get_successor(node):
    ans = leftmost_at_right(node)
    if ans != None:
        return ans
    # loop until find out if prev node is cur node's left subtree
    cur = node.parent
    prev = node
    while cur != None:
        if cur.left is prev:
            break
        prev = cur
        cur = cur.parent
    return cur


def test_func():
    N = None
    root = TreeNode.create_tree([1,2,4,N,N,5,N,N,3,6,N,N,7,N,N])

    # a_node = left most node at right subtree
    a_node = root.find_node(6)
    assert a_node is get_successor(root)

    # a_node = its right node
    q_node = root.find_node(2)
    a_node = root.find_node(5)
    assert a_node is get_successor(q_node)

    # a_node = its parent
    q_node = root.find_node(4)
    a_node = root.find_node(2)
    assert a_node is get_successor(q_node)

    # a_node = its parent's parent
    q_node = root.find_node(5)
    a_node = root.find_node(1)
    assert a_node is get_successor(q_node)

    # a_node = None
    q_node = root.find_node(7)
    a_node = None
    assert a_node == get_successor(q_node)
