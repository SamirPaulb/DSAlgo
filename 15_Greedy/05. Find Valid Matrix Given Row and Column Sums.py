# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
'''
Find the smallest rowSum or colSum, and let it be x. Place that number in the grid, and subtract x from rowSum and colSum. Continue until all the sums are satisfied.
'''

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        res = [[0]*len(colSum) for i in range(len(rowSum))]
        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        
        return res
    
# Time: O(M * N)
# Space: O(M * N)