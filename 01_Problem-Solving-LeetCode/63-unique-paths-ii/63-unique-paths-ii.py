class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        
        dp = [[0]*(n) for i in range(m)]
        
        # Inisializing 0th row
        v = 1
        for j in range(n):
            # if any obstacle comes in single row then that row can not be a path
            if obstacleGrid[0][j] == 1:
                v = 0
                dp[0][j] = v
            else: 
                dp[0][j] = v
        
        
        v = 1
        for i in range(m):
             # if any obstacle comes in single colomn then that colomn can not be a path
            if obstacleGrid[i][0] == 1:
                v = 0
                dp[i][0] = v
            else:
                dp[i][0] = v
        
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
            
        return dp[-1][-1]