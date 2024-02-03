class Solution:
    def partitionString(self, s: str) -> int:
        words = set()
        chars = set()

        j = 0
        i = 0
        while i < len(s):
            if s[i] in chars:
                chars.clear()
                j += 1
            chars.add(s[i])
            i += 1
        return j + (len(chars) != 0)