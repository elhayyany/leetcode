class Solution:
    def addSpaces(self, line, nspace):
        for i in range(nspace):
            line[i % (len(line)-1)] += ' '
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        lsize = 0
        i = 0
        l = len(words)
        while i < l:
            line.append(words[i])
            lsize = len(words[i])
            i += 1
            while i < l and (maxWidth - lsize - 1 - len(words[i])) >= 0:
                line.append(words[i])
                lsize += len(words[i]) + 1
                i += 1
            if len(line) == 1 or i == l:
                line[len(line) - 1] += ' ' * (maxWidth - (len(line) + sum(map(len, line)) - 1))
            elif i < l:
                    self.addSpaces(line, maxWidth - (len(line) + sum(map(len, line)) - 1))
            res.append(' '.join(line))
            line = []
        return res