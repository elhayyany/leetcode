"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        que = deque()
        root = Node(node.val)
        dic = {node.val:root}
        que.append(node)
        while len(que):
            nd = que.popleft()
            rt = dic[nd.val]
            for n in nd.neighbors:
                if n.val not in dic:
                    tnd = Node(n.val)
                    dic[n.val] = tnd
                    que.append(n)
                rt.neighbors.append(dic[n.val])
        return root
        