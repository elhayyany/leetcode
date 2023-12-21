# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, p: List[int], ino: List[int]) -> Optional[TreeNode]:
        i = 0
        j = len(ino) - 1
        dic = {a:i for i, a in enumerate(ino)}
        k = 0
        def builder(i, j):
            nonlocal k
            if k == len(p) or i > j:
                return
            node = TreeNode(p[k])
            k += 1
            node.left = builder(i, dic[node.val]-1)
            node.right = builder(dic[node.val] + 1, j)
            return node
            
        return builder(i, j)