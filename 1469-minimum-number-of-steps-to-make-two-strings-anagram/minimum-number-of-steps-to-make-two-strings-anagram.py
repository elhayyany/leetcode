class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sDict = {c:0 for c in s}
        tDict = {c:0 for c in t}
        for c in s:
            sDict[c] +=1
        for c in t:
            tDict[c]+=1
        for key in sDict.keys():
            sDict[key] = sDict[key] - tDict[key] if key in tDict else sDict[key]
            if sDict[key] < 0:
                sDict[key] = 0
        return sum(sDict.values())
