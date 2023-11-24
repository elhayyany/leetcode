class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lf = 0
        rg =   len(numbers) - 1
        while lf < rg:
            if numbers[lf] + numbers[rg] == target:
                return [lf+1, rg+1]
            elif numbers[lf] + numbers[rg] > target:
                rg -= 1
            else:
                lf += 1