class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) // 4
        p = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                p += 1
                if p >= quarter:
                    return arr[i]
                continue
            p = 0
        return arr[0]