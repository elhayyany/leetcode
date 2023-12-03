class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        res = 0
        pre = 0
        while i < j:
            print(i, j)
            res = max(min(nums[i], nums[j]) * (j - i), res)
            if nums[i] < nums[j]:
                pre = nums[i]
                i += 1
                while nums[i] < pre and i < j:
                    i += 1
            elif nums[i] > nums[j]:
                pre = nums[j]
                j -= 1
                while pre > nums[j] and i < j:
                    j -= 1
            else:
                j -= 1
        return res