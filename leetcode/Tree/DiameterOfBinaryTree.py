class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def diameter(root: TreeNode):
    longest = [0]   # longest = 0
    
    def dfs(node: TreeNode):
        if node is None:
            return -1
            
        left = dfs(node.left)
        right = dfs(node.right)

        state = max(left, right) + 1
        longest[0] = max(longest[0], left + right + 2)    # longest = max(longest, left + right + 2)

        return state

    dfs(root)
    return longest[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.left.left.left.left = TreeNode(9)
root.left.right.right.left = TreeNode(10)
root.left.right.right.right = TreeNode(11)
root.left.right.right.right.left = TreeNode(12)
root.left.right.right.right.right = TreeNode(13)
print(diameter(root))


# --------------------------------------------
# 이진트리(BinaryTree)를 처리할 때는 두 가지를 기억하자
# 1. 상태값
# 2. 존재하지 않는 노드 : -1
# --------------------------------------------