class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        while n // 10 != 0:
            k = str(n)
            n = sum(int(m)**2 for m in k)
        return n == 1 or n == 7