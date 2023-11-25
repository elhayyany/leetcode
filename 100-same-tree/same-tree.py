# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, left, right):
        if left and right and left.val == right.val:
            return self.dfs(left.left, right.left) and self.dfs(left.right, right.right)
        elif not left and not right:
            return True
        return False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)
        