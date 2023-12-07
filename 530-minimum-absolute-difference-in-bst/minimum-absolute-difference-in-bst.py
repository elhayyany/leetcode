# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, lst):
        if not root:
            return
        self.dfs(root.left,lst)
        lst.append(root.val)
        self.dfs(root.right,lst)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst = []
        self.dfs(root, lst)
        res = lst[1] - lst[0]
        for i in range(1, len(lst) - 1):
            if lst[i + 1] - lst[i] < res:
                res = lst[i + 1] - lst[i]
        return res