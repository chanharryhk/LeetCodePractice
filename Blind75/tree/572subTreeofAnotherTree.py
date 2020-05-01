# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def helper(s, t):
            if s and t:
                if s.val == t.val:
                    return helper(s.left, t.left) and helper(s.right, t.right)
            elif not s and not t:
                return True

        if s:
            if helper(s,t): 
                return True
            # Why doesnt this work??? HUH?            
            # if s.val == t.val:
            #     return helper(s, t)
            return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
        
        