# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def countSubTrees(root):
            if not root:
                return 0
            i = 0
            tem = root
            while tem:
                tem = tem.left
                i += 1
            tem = root
            j = 0
            while tem:
                j += 1
                tem = tem.right
            if i == j:
                return (2 ** j) -1
            return countSubTrees(root.left) + countSubTrees(root.right) + 1
        return countSubTrees(root)