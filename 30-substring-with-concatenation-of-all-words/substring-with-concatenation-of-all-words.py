class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        st = {}
        for word in words:
            st[word] = st.get(word,0) + 1
        l = len(words[0])
        sumLen = len(words[0]) * len(words)
        j = 0
        res = []
        for i in range(len(s) - sumLen + 1):
            if s[i:i+l] in st:
                founded = {}
                founded[s[i:i+l]] = 1
                j = i+l
                while j < len(s):
                    if s[j:j+l] not in st:
                        break
                    founded[s[j:j+l]] = founded.get(s[j:j+l], 0) + 1
                    if founded[s[j:j+l]] > st[s[j:j+l]]:
                        break
                    j += l
            if (j - i) >= sumLen:
                res.append(i)
        return res