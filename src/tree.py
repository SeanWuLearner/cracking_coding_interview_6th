
class TreeNode():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    @staticmethod
    def create_tree(preorder_list):
        '''Return the root tree node according to given preorder list'''
        def helper(parent):
            try:
                val = next(vals)
            except:
                return None
            if val == None:
                return None

            node = TreeNode(val, parent=parent)
            node.left = helper(node)
            node.right = helper(node)
            return node
        vals = iter(preorder_list)
        return helper(None)

    def find_node(self, val):
        def helper(node):
            if node == None:
                return None
            if node.val == val:
                return node
            res_l = helper(node.left)
            return helper(node.right) if res_l == None else res_l
        return helper(self)

    def __str__(self):
        '''Return the preorder list of this node'''
        def helper(node):
            if node == None:
                vals.append('N,')
                return
            vals.append(str(node.val)+',')
            helper(node.left)
            helper(node.right)

        vals = []
        helper(self)
        return ''.join(vals)

    def draw(self):
        '''dump the whole tree structure using lines'''
        buf = []
        self._draw_helper(buf, '', '')
        print(''.join(buf))

    def _draw_helper(self, buf, prefix, child_prefix):
        buf += prefix
        buf += str(self.val)
        buf += '\n'
        for c in self.childs:
            if c==None:
                continue
            if c is not self.childs[-1]:
                c._draw_helper(buf, child_prefix + "├── ", child_prefix+"│   ")
            else:
                c._draw_helper(buf, child_prefix + "└── ", child_prefix+"    ")

    @property
    def childs(self):
        return [self.right, self.left]

    @property
    def height(self):
        def helper(node):
            if node == None:
                return 0
            l_height = helper(node.left)
            r_height = helper(node.right)
            return 1 + max(l_height, r_height)
        return helper(self)

def test_tree():
    N = None
    l = [1,2,4,N,N,5,N,N,3,6,N,N,7,N,N]
    node = TreeNode.create_tree(l)
    node.draw()
    print(node)
    print(f'height = {node.height}')

if __name__ == "__main__":
    test_tree()