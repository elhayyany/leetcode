class Solution:
    def isInRow(self, n, row):
        print(row)
        min = 0
        max = len(row) - 1
        mid = 0
        while min <= max:
            mid = (min + max) // 2
            if n == row[mid]:
                return True
            elif n < row[mid]:
                max = mid - 1
            else:
                min = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        min = 0
        max = len(matrix) - 1
        mid = 0
        while min <= max:
            mid = (min + max) // 2
            if target <= matrix[mid][-1] and target >= matrix[mid][0]:
                return self.isInRow(target, matrix[mid])
            elif target > matrix[mid][-1]:
                min = mid + 1
            else:
                max = mid - 1
        return False