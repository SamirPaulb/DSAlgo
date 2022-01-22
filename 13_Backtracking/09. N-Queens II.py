# https://leetcode.com/problems/n-queens-ii/

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