class Solution:
    def markVisited(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid)\
        or j == len(grid[i]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.markVisited(grid, i, j+1)
        self.markVisited(grid, i, j-1)
        self.markVisited(grid, i+1, j)
        self.markVisited(grid, i-1, j)

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.markVisited(grid, i, j)
                    res += 1
        return res