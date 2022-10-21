class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[2**31]*n for i in range(n)]
        for u, v, w in edges:
            dp[u][v] = w
            dp[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j: 
                        dp[i][j] = 0
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        
        res = 0
        min_reach = n
        for i in range(n):
            i_reach = 0
            for j in range(n):
                if dp[i][j] <= distanceThreshold:
                    i_reach += 1
            print(i_reach)
            if i_reach <= min_reach:
                res = i
                min_reach = i_reach
        
        return res