class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArray2BST(nums: list) -> TreeNode:
    if not nums:
        return None
    
    mid = len(nums) // 2

    node = TreeNode(nums[mid])
    node.left = sortedArray2BST(nums[:mid])
    node.right = sortedArray2BST(nums[mid+1:])

    return node
