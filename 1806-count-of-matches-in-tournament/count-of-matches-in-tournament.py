class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            if (n % 2) == 0:
                n /= 2
                res += n
            else:
                n = (n - 1) / 2
                res += n
                n += 1
        return int(res)