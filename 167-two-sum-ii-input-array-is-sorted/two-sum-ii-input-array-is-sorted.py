class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lf = 0
        rg =   len(numbers) - 1
        tmp = 0
        while lf < rg:
            tem = numbers[lf] + numbers[rg]
            if tem == target:
                return [lf+1, rg+1]
            elif tem > target:
                rg -= 1
            else:
                lf += 1