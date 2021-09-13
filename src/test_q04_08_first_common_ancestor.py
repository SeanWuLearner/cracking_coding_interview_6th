from tree import TreeNode



def cover(root, node):
    if root == None:
        return False
    if root is node:
        return True
    return cover(root.left, node) or cover(root.right, node)


### solution from book: bubble up finding to optimized the run time
#       Return p if root's subtree includes p (and not q)
#       Return q if root's subtree includes q (and not p)
#       Return None if neither of them in root's subtree
#       Return common ancestor of p and q

def common_ancestor(root, node1, node2):
    if root==None:
        return None
    if node1 is node2:
        return node1
    if cover(root, node1)==False and cover(root, node2)==False:
        return False

    def helper(root, node1, node2):
        if root==None:
            return None

        rx = helper(root.left, node1, node2)
        ry = helper(root.right, node1, node2)

        if rx!=None and ry!=None:
            return root
        if root is node1 or root is node2:
            return root
        return rx if rx!=None else ry

    return helper(root, node1, node2)


## My naive solution: literally just search thru it. Each nodes might be visied multiple times.
# def common_ancestor(root, node1, node2):
#     if root==None:
#         return None
#     if node1 is node2:
#         return node1
#     if cover(root, node1)==False and cover(root, node2)==False:
#         return False

#     def helper(root, node1, node2):
#         node_in_l = node_in_r = 0

#         if cover(root.left, node1):
#             node_in_l+=1
#         else:
#             node_in_r+=1

#         if cover(root.left, node2):
#             node_in_l+=1
#         else:
#             node_in_r+=1

#         if node_in_l==1 and node_in_r==1:
#             return root
#         if node_in_l==2:
#             return common_ancestor(root.left, node1, node2)
#         if node_in_r==2:
#             return common_ancestor(root.right, node1, node2)
#         # the case that either node1 or node2 is the root
#         return node1 if node1 is root else node2

#     return helper(root, node1, node2)



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
    root =  TreeNode.create_tree([1,2,4,N,N,5,N,N,3,6,N,N,7,N,N])
    # the ancestor of 4 and 7 is 1
    ancestor = root.find_node(1)
    node1 = root.find_node(4)
    node2 = root.find_node(7)
    assert ancestor is common_ancestor(root, node1, node2)
    # the ancestor of 4 and 5 is 2
    ancestor = root.find_node(2)
    node1 = root.find_node(4)
    node2 = root.find_node(5)
    assert ancestor is common_ancestor(root, node1, node2)
    # the ancestor of 4 and 1 is 1
    ancestor = root.find_node(1)
    node1 = root.find_node(4)
    node2 = root.find_node(1)
    assert ancestor is common_ancestor(root, node1, node2)
    # the ancestor of 4 and 4 is 4
    ancestor = root.find_node(4)
    node1 = root.find_node(4)
    node2 = root.find_node(4)
    assert ancestor is common_ancestor(root, node1, node2)
