# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        cur = 1
        nxt = 0
        res = []
        tem = []
        que = deque()
        que.append(root)
        while len(que):
            for i in range(cur):
                a = que.popleft()
                if a.left:
                    que.append(a.left)
                    nxt += 1
                if a.right:
                    que.append(a.right)
                    nxt += 1
                tem.append(a)
            res.append(tem)
            tem = []
            cur = nxt
            nxt = 0
        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j] = res[i][j].val
        return res