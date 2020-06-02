# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        def dfs(root, string):
            if root:
                temp = string + str(root.val)
                if not root.left and not root.right:
                    ans.append(temp)
                    
                dfs(root.left, temp + "->")
                dfs(root.right, temp + "->")
        
        dfs(root, "")
        return ans
        