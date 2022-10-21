class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = set()
        col = set()
        posDiag = set()
        negDiag = set()
        board = [['.']*n for i in range(n)]
        res = []
        
        def dfs(i):
            if i >= n: 
                s = ["".join(board[i]) for i in range(n)]
                res.append(s)
                return
            
            for j in range(n):
                if j in col or (i+j) in posDiag or (i-j) in negDiag: continue
                
                col.add(j)
                posDiag.add(i+j)
                negDiag.add(i-j)
                board[i][j] = "Q"

                dfs(i+1)

                col.remove(j)
                posDiag.remove(i+j)
                negDiag.remove(i-j)
                board[i][j] = "."
        
        dfs(0)
        return res
