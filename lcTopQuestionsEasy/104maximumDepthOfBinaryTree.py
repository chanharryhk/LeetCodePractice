class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(currNode, depth):
            if currNode:
                return max(dfs(currNode.left, depth+1), dfs(currNode.right, depth+1))
            return depth
        return dfs(root, 0)