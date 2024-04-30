from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hashes = []
        res = []
        dic = {}
        for word in words:
            hashes.append(dict(Counter(word)))
        for k, v in hashes[0].items():
            for i in range(1, len(hashes)):
                if k not in hashes[i]:
                    v = 0
                    break
                v = min(v, hashes[i][k])
            for i in range(v):
                res.append(k)
        return res
                