class Solution:
    def totalMoney(self, n: int) -> int:
        Reste = n % 7
        Weeks = n // 7
        return int((7 * (7 * Weeks + Weeks**2) + Reste * (2 * Weeks + Reste + 1)) / 2)