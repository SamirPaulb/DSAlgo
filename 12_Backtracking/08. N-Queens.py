# https://leetcode.com/problems/n-queens
''' 
queen attack horizontally, vertically, is both positive diagonal and negetive diagonal.
we travers row-wise and keep a track of the above parameters in a set and make sure no 2 queens 
comes in each other direction.
'''
# DFS  => taking variables as global variables
# https://www.youtube.com/watch?v=Ph95IHmRp5M

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        res = []
        chessboard = [["."]*n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in chessboard]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or r + c in posDiag or r - c in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                chessboard[r][c] = "Q"
                
                backtrack(r + 1)
                
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                chessboard[r][c] = "."
        
        backtrack(0)
        return res

# Time Complexity: O( N^2 )
# Space Complexity: O( N^2 )