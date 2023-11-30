class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = 1
        for i in range(len(digits) - 1, -1, -1):
            if k and digits[i] == 9:
                digits[i] = 0
            elif k:
                digits[i] += 1
                k = 0
            else:
                return digits
        if k:
            digits.insert(0,1)
        return digits