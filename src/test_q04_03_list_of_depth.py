from tree import TreeNode

def list_of_depths(root):
    def helper(node, level):
        if node == None:
            return
        if len(ans) < level:
            ans.append([node.val])
        else:
            ans[level-1].append(node.val)
        helper(node.left, level+1)
        helper(node.right, level+1)

    ans = []
    helper(root, 1)
    return ans


def test_func():
    ans = [
        [1],
        [2,3],
        [4,5,6,7]
    ]
    node = TreeNode.create_tree([1,2,4,None,None,5,None,None,3,6,None,None,7,None,None])
    assert ans == list_of_depths(node)

    ans = [
        [1],
        [2,3],
        [4,7]
    ]
    node = TreeNode.create_tree([1,2,4,None,None,None,3,None,7,None,None])
    assert ans == list_of_depths(node)
