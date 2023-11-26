class Solution:
    def search(self, board, word, i, j, ch):
        if ch == len(word):
            return True
        if  j == -1 or i == len(board) or\
            j == len(board[0]) or  i == -1 or\
            board[i][j] != word[ch]:
            return False
        k = board[i][j]
        board[i][j] = '.'
        if  self.search(board, word, i, j + 1, ch+1) or\
            self.search(board, word, i, j - 1, ch+1) or\
            self.search(board, word, i - 1, j, ch+1) or\
            self.search(board, word, i + 1, j, ch+1):
            return True
        board[i][j] = k
        return False
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.search(board, word, i, j, 0):
                        return True
        return False