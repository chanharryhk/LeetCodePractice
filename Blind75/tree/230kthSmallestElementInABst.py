# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = -1
    count = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if root:
                dfs(root.left)
                self.count += 1
                if self.count == k:
                    self.ans = root.val
                    return
                print(root.val)
                dfs(root.right)
        dfs(root)
        return self.ans
