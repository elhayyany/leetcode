class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 0
        factors = []
        for j in range(1, int(math.sqrt(n)) + 1):
            if n%j == 0:
                if j**2 != n:
                    factors.append(n//j)
                i += 1
                if i == k:
                    return j
        if k - i <= len(factors):
            return factors[i-k]
        return -1