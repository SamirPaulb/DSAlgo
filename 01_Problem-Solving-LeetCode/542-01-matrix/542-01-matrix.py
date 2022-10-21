class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[2**31]*n for i in range(m)]
        
        def get(i, j):
            if not 0<=i<len(res) or not 0<=j<len(res[0]):
                return 2**31
            return res[i][j]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                elif i == 0 or j == 0:
                    res[i][j] = min(get(i-1, j), get(i, j-1)) + 1
                else:
                    res[i][j] = min(res[i-1][j], res[i][j-1]) + 1
        print(res)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] == 0:
                    res[i][j] = 0
                elif i == m-1 or j == n-1:
                    res[i][j] = min(res[i][j], min(get(i+1, j), get(i, j+1)) + 1)
                else:
                    res[i][j] = min(res[i][j], min(res[i+1][j], res[i][j+1]) + 1)
        
        return res
                    
                    
                    