class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        a = 0
        for i in range(len(gain)):
           a += gain [i]
           if h < a:
                h = a
        return h
 