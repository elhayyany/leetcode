class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        j = 1
        k = 0
        for i in st:
            if i - 1 not in st:
                j = 1
                k = i + 1
                while k in st:
                    k += 1
                    j += 1
                res = max(res, j)
        return res
                
            
                