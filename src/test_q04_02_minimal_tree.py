from tree import TreeNode

def minimal_tree(arr):
    def build_tree(start, end):
        if start < 0 or start == end:
            return None
        mid = (start + end) // 2
        left = build_tree(start, mid)
        right = build_tree(mid+1, end)
        return TreeNode(arr[mid], left, right)

    return build_tree(0, len(arr))


def test_func():
    assert 2 == minimal_tree([1,2,3]).height
    assert 3 == minimal_tree([1,2,3,4,5,6,7]).height
    assert 4 == minimal_tree([1,2,3,4,5,6,7,8]).height
    assert 4 == minimal_tree([1,2,3,4,5,6,7,8,9,10,11,12]).height


