# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        i = 0
        j = len(inorder) - 1
        dic = {a:i for i,a in enumerate(inorder)}
        k = j
        def builder(i, j):
            nonlocal k
            if k < 0 or i > j:
                return
            node = TreeNode(postorder[k])
            k -= 1
            node.right = builder(dic[node.val] + 1, j)
            node.left = builder(i, dic[node.val] - 1)
            return node
        return builder(i, j)