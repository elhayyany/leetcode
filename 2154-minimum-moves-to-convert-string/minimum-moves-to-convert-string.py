class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        res = 0
        while i < len(s):
            if s[i] == 'X':
                res += 1
                i += 2
            i += 1
        return res