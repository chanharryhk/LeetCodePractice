# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            currLevel = []
            levelLen = len(q)
            for i in range(levelLen):
                currNode = q.popleft()
                currLevel.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            res.append(currLevel)
        return res
            