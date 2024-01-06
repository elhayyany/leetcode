# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        mp = set()
        def dfs(root,mp, k):
            if not root or len(mp) == k:
                return -1
            if root.left:
                dfs(root.left, mp, k)
            if len(mp) == k:
                return 
            mp.add(root.val)
            if root.right:
                dfs(root.right, mp, k)
            if len(mp) == k:
                return 
            mp.add(root.val)
            return
        dfs(root, mp, k)
        return max(mp)