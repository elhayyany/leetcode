class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        dic = {i:-1 for i in nums}
        g = 0
        for i in dic.keys():
            g = i + 1
            while g in dic and dic[g] == -1:
                dic[g] = 0
                g += 1
            dic[i] = g - i + (0 if g not in dic else dic[g])
            print(dic[i])
        return max(dic.values())
                