# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []   
        ans = []
        queue = [root]
        while queue:
            count = len(queue)
            subAns = []
            while count > 0:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                subAns.append(node.val)
                count -= 1
            ans.append(subAns)
        return ans
        