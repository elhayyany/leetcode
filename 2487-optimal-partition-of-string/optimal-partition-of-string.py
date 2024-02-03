class Solution:
    def partitionString(self, s: str) -> int:
        chars = set()
        j = 0

        for i in range(len(s)):
            if s[i] in chars:
                chars.clear()
                j += 1
            chars.add(s[i])
        return j + 1