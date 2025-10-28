class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestUniValue(root: TreeNode):
    longest = [0]

    def dfs(node: TreeNode):
        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        if node.left and node.val == node.left.val:
            left += 1
        else:
            left = 0

        if node.right and node.val == node.right.val:
            right += 1
        else:
            right = 0

        longest[0] = max(longest[0], left+right)
        return max(left, right)

    dfs(root)
    return longest[0]

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

print(longestUniValue(root))