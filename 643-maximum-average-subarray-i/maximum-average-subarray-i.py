class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm = sum(nums[:k])
        avg = sm
        for i in range(len(nums) - k):
            sm += nums[k + i] - nums[i]
            if sm > avg:
                avg = sm
        return avg / k