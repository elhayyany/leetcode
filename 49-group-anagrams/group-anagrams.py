class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = [''.join(sorted(s)) for s in strs]
        dic = {}
        j = 0
        for r in s:
            if r in dic:
                dic[r].append(strs[j])
            else:
                dic[r] = [strs[j]]
            j += 1
        return [val for val in dic.values()]