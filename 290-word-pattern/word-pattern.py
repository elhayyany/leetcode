import itertools
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = itertools.zip_longest([c for c in pattern], s.split())
        dic = {}
        for p, w in t:
            print(w)
            if p in dic:
                if w != dic[p]:
                    return False
            elif w is None or p is None:
                return False
            else:
                dic[p] = w
        return len(set(dic.values())) == len(dic.keys())
