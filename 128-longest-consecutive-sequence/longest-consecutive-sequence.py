class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        j = 1
        for i in st:
            if i - 1 not in st:
                j = 1
                while i + j in st:
                    j += 1
                res = max(res, j)
        return res
                
            
                