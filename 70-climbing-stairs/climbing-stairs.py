class Solution:
    def climbStairs(self, n: int) -> int:
        mp = {}
        def fb(n):
            if n < 4:
                return n
            if n in mp:
                return mp[n]
            mp[n] = fb(n - 1) + fb(n - 2)
            return mp[n]
        return fb(n)