class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        totalSum = sum(nums)
        leftSum = 0
        l = len(nums)
        res = [0] * l
        for i in range(l):
            res[i] = (totalSum - leftSum) - (nums[i] * (l - i)) + i * nums[i] - leftSum
            leftSum += nums[i]
        return res