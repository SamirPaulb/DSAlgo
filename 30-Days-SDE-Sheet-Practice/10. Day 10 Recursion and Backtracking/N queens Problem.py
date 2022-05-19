# https://leetcode.com/problems/n-queens/
''' 
queen attack horizontally, vertically, is both positive diagonal and negetive diagonal.
we travers row-wise and keep a track of the above parameters in a set and make sure no 2 queens 
comes in each other direction.
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDig = set()
        negDig = set()
        board = [['.']*n for i in range(n)]
        res = []
        
        def backtrack(r):
            if r >= n:
                res.append([''.join(board[i]) for i in range(n)])
                return
            
            for i in range(n):
                if i in col or (r+i) in posDig or (r-i) in negDig:
                    continue
                    
                board[r][i] = 'Q' 
                col.add(i)
                posDig.add(r+i)
                negDig.add(r-i)
                
                backtrack(r+1)
                
                board[r][i] = '.'
                col.remove(i)
                posDig.remove(r+i)
                negDig.remove(r-i)
        
        
        backtrack(0)
        return res

# Time Complexity: O( N^2 )
# Space Complexity: O( N^2 )