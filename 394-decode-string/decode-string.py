class Solution:
    def rec(self, s):
        text = []
        ln = len(s)
        i = 0
        while i < ln:
            if s[i] == '[':
                t, j = self.rec(s[i+1:])
                tem = ''
                while text and text[-1].isdigit():
                    tem = text.pop() + tem
                text += int(tem) * t
                i += j
            elif s[i] == ']':
                return text, i+1
            else:
                text.append(s[i])

            i += 1
        return text, i
    def decodeString(self, s: str) -> str:
        t, j = self.rec(s)
        return ''.join(t)
