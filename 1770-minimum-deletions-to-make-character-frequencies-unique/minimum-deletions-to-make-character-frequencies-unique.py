class Solution:
    def minDeletions(self, s: str) -> int:
        dic = {a:0 for a in s}
        for a in s:
            dic[a] += 1
        sortedFrequencies = sorted(list(dic.values()))
        st =  set(sortedFrequencies)
        stack = []
        for i in range(1, sortedFrequencies[-1]):
            if i not in st:
                stack.append(i)
        pre = sortedFrequencies[-1]
        res = 0
        i = len(sortedFrequencies) - 2
        while i > -1:
            if stack and sortedFrequencies[i] < stack[-1]:
                    stack.pop(-1)
                    continue
            if sortedFrequencies[i] == pre:
                if stack:
                    res += pre - stack[-1]
                    stack.pop(-1)
                else:
                    res += pre
            pre = sortedFrequencies[i]
            i -= 1
        return res