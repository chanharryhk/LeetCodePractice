# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(currNode, minNode, maxNode):
            if currNode:
                if minNode:
                    if minNode.val >= currNode.val:
                        return False
                if maxNode:
                    if maxNode.val <= currNode.val:
                        return False
                return dfs(currNode.right, currNode, maxNode) and dfs(currNode.left, minNode, currNode)
            return True
        return dfs(root, None, None)