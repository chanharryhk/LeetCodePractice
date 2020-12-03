# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(node1, node2):
            if node1 and node2:
                if node1.val == node2.val:
                    return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
                else:
                    return False
            elif not node1 and not node2:
                return True
        return dfs(root, root)