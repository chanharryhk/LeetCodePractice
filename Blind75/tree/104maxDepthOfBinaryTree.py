# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    depth = 0
    def maxDepth(self, root: TreeNode) -> int:
        return self.helper(root, 0)
            
    def helper(self, root: TreeNode, depth) -> int:
        if root:
            depth += 1
            return max(self.helper(root.left, depth), self.helper(root.right, depth))
        return depth