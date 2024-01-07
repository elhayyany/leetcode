class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        Imp = set()
        def back(i):
            print(i, len(s), Imp)
            if i in Imp:
                return False
            if i == len(s):
                return True
            for w in wordDict:
                if s[i:].startswith(w):
                    if back(i+len(w)):
                        return True
            Imp.add(i)
            return False
        return back(0)