class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestUniValue(root: TreeNode):
    longest = [0]

    def dfs(node: TreeNode, k):
        longest[0] = max(longest[0], k)
        
        if node.left:
            if node.val == node.left.val:
                dfs(node.left, k+1)
            else:
                dfs(node.left, 1)

        if node.right:
            if node.val == node.right.val:
                dfs(node.right, k+1)
            else:
                dfs(node.right, 1)

    dfs(root, 1)
    return longest[0]

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

print(longestUniValue(root))