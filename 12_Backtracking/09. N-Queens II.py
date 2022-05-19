# https://leetcode.com/problems/n-queens-ii/
''' 
queen attack horizontally, vertically, is both positive diagonal and negetive diagonal.
we travers row-wise and keep a track of the above parameters in a set and make sure no 2 queens 
comes in each other direction.
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        
        row = set()
        col = set()
        posDiag = set()
        negDiag = set()
        
        def backtrack(r):
            if r == n: 
                self.res += 1
            
            for c in range(n):
                if r in row or c in col or r+c in posDiag or r-c in negDiag:
                    continue
                
                row.add(r)
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                
                backtrack(r+1)
                
                row.remove(r)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        
        backtrack(0)
        return self.res

# Time Complexity: O( N^2 )
# Space Complexity: O( N^2 )