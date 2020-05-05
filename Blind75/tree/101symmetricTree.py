# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(pre, preMirror):
            if pre and preMirror:
                if pre.val == preMirror.val:
                    return helper(pre.left, preMirror.right) and helper(pre.right, preMirror.left)
            elif not pre and not preMirror:
                return True
        
        if not root:
            return True    
        return helper(root, root)    
        