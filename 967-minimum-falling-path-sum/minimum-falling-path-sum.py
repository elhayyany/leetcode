class Solution:
    def minPath(self, ps, matrix, tmpPs, i, j):
        ps[j] = matrix[i][j]+ min( tmpPs[j],  tmpPs[j - 1] if j > 0 else tmpPs[j],  tmpPs[j + 1] if j < (len(matrix) - 1) else tmpPs[j])
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        pathSum = matrix[-1]
        for i in range(len(matrix) - 2, -1, -1):
            tmpPs = pathSum[:]
            prev = 0
            for j in range(len(matrix)):
                tmp = pathSum[j]
                pathSum[j] = matrix[i][j] + min(
                pathSum[j],
                prev if j > 0 else pathSum[j],
                pathSum[j + 1] if j < (len(matrix) - 1) else pathSum[j]
                )
                prev = tmp
        return min(pathSum)