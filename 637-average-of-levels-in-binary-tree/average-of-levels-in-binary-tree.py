# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        mp = {}
        arr = []
        def dfs(root, mp, level):
            if not root:
                return
            mp[level] = mp.get(level, 0) + 1
            if len(arr) <= level:
                arr.append(root.val)
            else:
                arr[level] += root.val
            dfs(root.right, mp, level+1)
            dfs(root.left, mp, level+1)
        dfs(root, mp, 0)
        for i in range(len(mp)):
            arr[i] = arr[i] / mp[i]
        return arr