class Solution:
    def search(self, board, word, i, j, ch, visited):
        if ch == len(word):
            return True
        if (i, j) in visited or i == -1 or j == -1 or i == len(board) or j == len(board[0]) \
            or board[i][j] != word[ch]:
            ch -= 1
            return False
        visited.add((i, j))
        if self.search(board, word, i, j + 1, ch+1, visited) or self.search(board, word, i, j - 1, ch+1, visited) or self.search(board, word, i - 1, j, ch+1, visited) or self.search(board, word, i + 1, j, ch+1, visited):
            return True
        visited.remove((i,j))
        return False
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.search(board, word, i, j, 0, set()):
                        return True
        return False