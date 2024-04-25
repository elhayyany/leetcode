class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        res = 0
        hp = sorted(h, reverse=True)
        for i in range(k):
            res += (hp[i] - i) if (hp[i] - i) > 0 else 0
        return res