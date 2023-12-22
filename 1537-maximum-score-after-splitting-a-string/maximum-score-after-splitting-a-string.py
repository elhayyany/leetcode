class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for c in s:
            if c == '1':
                ones += 1
        ziros = 0
        mx = 0
        for c in range(len(s) - 1):
            if s[c] == '0':
                ziros += 1
            else:
                ones -= 1
            mx = max(ziros + ones, mx)
        return mx