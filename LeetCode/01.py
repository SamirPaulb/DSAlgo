class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])
        for i in range(n):  # row
            for j in range(n):   # column
                a = board[i][j]
                if a == ".":
                    continue
                # check column
                for k in range(n):
                    if a == board[j][k] and k != j:
                        return False
                # check rows
                for k in range(n):
                    if a == board[k][j] and k != j:
                        return False
                    
                #check gride
                xi = i/3*3 # rows of grid
                xj = j/3*3 # column of grid
                    
                for p in range(xi,xi+3):
                    for q in range(xj,xj+3):
                        if board[i][j] == board[p][q] and xi != p and xj != q:
                            return False
        return True


