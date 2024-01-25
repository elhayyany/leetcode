class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        que = deque([(0, 0, 1)])
        visited = set((0, 0))
        dirs = [-1, 0, 1, 1, 1, 0, -1, -1, 0, 1, 1, 1, 0, -1, -1, -1]
        while que:
            x, y, l = que.popleft()
            if min(x, y) < 0 or max(x, y) == len(grid) or grid[x][y]:
                continue
            if x == len(grid) -1 and x == y:
                return l
            for i in range(8):
                if (x+dirs[i], y+dirs[~i]) not in visited:
                    que.append((x+dirs[i], y+dirs[~i], l+1))
                    visited.add((x+dirs[i], y+dirs[~i]))
        return -1