class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {'2' : ['a', 'b', 'c'],
                '3' : ['d', 'e', 'f'],
                '4' : ['g', 'h', 'i'],
                '5' : ['j', 'k', 'l'],
                '6' : ['m', 'n', 'o'],
                '7' : ['p', 'q', 'r', 's'],
                '8' : ['t', 'u', 'v'],
                '9' : ['w', 'x', 'y', 'z']
            }
        res = []
        def backtrack(digits, r):
            if not digits:
                res.append(r)
                return
            for c in dic[digits[0]]:
                backtrack(digits[1:], r + c)
        backtrack(digits, '')
        return res