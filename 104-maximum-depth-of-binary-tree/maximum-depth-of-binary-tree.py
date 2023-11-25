# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, i):
        if root:
            return max(self.dfs(root.right,i+1), self.dfs(root.left,i+1))
        return i
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)