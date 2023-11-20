class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s
        dic = {}
        for i in range(n):
            dic[i] = ''
        h = 0
        r = 0
        for i in range(len(s)):
            dic[r] +=  s[i]
            r = r + 1 if h % 2 else r - 1
            if r < 0 or r == n:
                r = 1 if r < 0 else  n - 2
                h += 1
        for i in range(1, n):
            dic[0] += dic[i]
        return dic[0]