class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def is_increasing(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]: return False
            return True
        i = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return is_increasing(nums[:i] + nums[i + 1:]) or is_increasing(nums[:i-1]+nums[i:])
        return True