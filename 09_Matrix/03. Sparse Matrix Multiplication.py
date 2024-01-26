# https://www.lintcode.com/problem/654/
# https://leetcode.com/problems/sparse-matrix-multiplication/

class Solution:
    def multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        aRow, aCol, bRow, bCol = len(a), len(a[0]), len(b), len(b[0])
        res = [[0]*bCol for _ in range(aRow)]
        for i in range(aRow):
            for j in range(bCol):
                for k in range(bRow):
                    res[i][j] += a[i][k] * b[k][j]
        return res 

# Time: O(aRow * bCol * bRow)
# Space: O(aRow * bCol)
