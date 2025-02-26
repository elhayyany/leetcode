class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        f = 0
        s = 0
        while s < ln:
            while f < ln and nums[f] != 0:
                f += 1
            s = f + 1
            while s < ln and nums[s] == 0:
                s += 1
            if s < ln:
                nums[f], nums[s] = nums[s], nums[f]
