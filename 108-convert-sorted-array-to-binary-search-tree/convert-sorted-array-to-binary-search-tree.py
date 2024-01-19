# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(nums, s, e):
            if s >= e:
                return
            node = TreeNode(nums[(s + e)//2])
            node.left = construct(nums, s, (s + e)//2)
            node.right = construct(nums, (s+e)//2 + 1, e)
            return node
        return construct(nums, 0, len(nums))