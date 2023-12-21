class Solution:
    def dfs(self, b, x, y, visited, toFlip, noFlip):
        if x < 0 or x == len(b[0]) or\
            y < 0 or y == len(b) or\
            (x,y) in noFlip:
            return False
        if (x, y) in visited or b[y][x] == 'X':
            return True
        visited.add((x,y))
        toFlip.add((x, y))
        return (self.dfs(b,x + 1,y,visited, toFlip, noFlip) and\
            self.dfs(b,x - 1,y,visited, toFlip, noFlip) and\
            self.dfs(b,x,y + 1,visited, toFlip, noFlip) and\
            self.dfs(b,x,y - 1,visited, toFlip, noFlip))
            
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        toFlip = set()
        noFlip = set()
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 'O' and board[y][x] not in visited:
                    if self.dfs(board, x, y, visited, toFlip, noFlip):
                        for i, j in toFlip:
                            board[j][i] = 'X'
                    else:
                        noFlip.update(toFlip)
                    toFlip.clear()

        