class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        removeFrom = 0
        for i in range(len(s)):
            if s[i] in dic:
                res = max(len(dic), res)
                for j in range(removeFrom, dic[s[i]]):
                    dic.pop(s[j])
                removeFrom = dic[s[i]] + 1
            dic[s[i]] = i
        return max(len(dic), res)