class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[]] * len(matrix[0])
        for i in range(len(matrix[0])):
            tem = [0] * len(matrix)
            for j in range(len(matrix)):
                tem[j] = matrix[j][i]
            res[i] = tem
        return res