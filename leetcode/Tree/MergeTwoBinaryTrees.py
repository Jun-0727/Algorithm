class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        val = self.val
        left = self.left
        right = self.right


def merge_trees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)

        node.left = merge_trees(t1.left, t2.left)
        node.right = merge_trees(t1.right, t2.right)
        
        return node
    else:
        return t1 or t2
    
