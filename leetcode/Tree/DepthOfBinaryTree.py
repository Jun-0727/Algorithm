from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3, None, None)
root.left = TreeNode(9, None, None)
root.right = TreeNode(20, None, None)
root.right.left = TreeNode(15, None, None)
root.right.right = TreeNode(7, None, None)

def maxDepth(root: TreeNode):
    if root is None:
        return 0
    
    que = deque([root])
    depth = 0
    
    while que:
        depth += 1
        for _ in range(len(que)):
            node = que.pop()
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

    return depth


print(maxDepth(root))
    