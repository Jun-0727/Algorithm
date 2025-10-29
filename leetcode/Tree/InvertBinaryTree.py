class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(node: TreeNode) -> TreeNode:
    if node:
        node.left, node.right = invert_tree(node.right), invert_tree(node.left)
        return node
    
    return None


from collections import deque

def invert_tree_bfs(root: TreeNode) -> TreeNode:
    que = deque([root])

    while que:
        node = que.popleft()
        if node:
            node.left, node.right = node.right, node.left
            que.append(node.left)
            que.append(node.right)
    
    return root