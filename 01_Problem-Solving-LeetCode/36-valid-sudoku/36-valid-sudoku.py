class Solution:
    def isValidSudoku(self, board):
        row = {i:set() for i in range(9)}
        col = {j:set() for j in range(9)}
        subbox = {(i//3, j//3): set() for j in range(9) for i in range(9)}
        
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == '.': continue
                if cur in row[i]: return False
                row[i].add(cur)
                if cur in col[j]: return False
                col[j].add(cur)
                key = (i//3, j//3)
                if cur in subbox[key]: return False
                subbox[key].add(cur)
        
        return True