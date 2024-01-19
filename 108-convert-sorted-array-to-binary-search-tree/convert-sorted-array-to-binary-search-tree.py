# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(nums):
            if not nums:
                return
            node = TreeNode(nums[len(nums)//2])
            node.left = construct(nums[:len(nums)//2])
            node.right = construct(nums[len(nums)//2 + 1:])
            return node
        return construct(nums)