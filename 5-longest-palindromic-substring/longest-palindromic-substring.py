class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0, 0]
        def get_index(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            if (j - i) > (res[1] - res[0]):
                res[0] = i + 1
                res[1] = j
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                get_index(i, i + 1)
            if i < (len(s) - 2) and s[i] == s[i + 2]:
                get_index(i, i + 2)
        if res == [0,0]:
            return s[0]
        return s[res[0]:res[1]]