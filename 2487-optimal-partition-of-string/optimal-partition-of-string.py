class Solution:
    def partitionString(self, s: str) -> int:
        chars = set()
        j = 0
        i = 0

        for i in range(len(s)):
            if s[i] in chars:
                chars.clear()
                j += 1
            chars.add(s[i])
            i += 1
        return j + 1