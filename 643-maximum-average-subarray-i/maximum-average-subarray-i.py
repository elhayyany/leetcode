class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm = sum(nums[:k])
        avg = sm / k
        for i in range(len(nums) - k):
            sm += nums[k] - nums[i]
            avg = max(avg, sm / (k-i))
            k += 1
        return avg