class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        dic = {}
        for i, val in enumerate(numbers):
            dic[val] = i + 1
        for i in numbers:
            if target - i in dic:
                res = [dic[i], dic[target - i]]
                if res[0] == res[1]:
                    res[0] -= 1
                return res
            