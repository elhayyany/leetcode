class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def count_palindrom(s, i, j):
            r = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return int((j - i) / 2)
        for i in range(len(s)):
            res += count_palindrom(s, i, i + 1)
            res += count_palindrom(s, i, i + 2)
        return res