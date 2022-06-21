# https://leetcode.com/problems/edit-distance/

# Recursive
class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        def solve(w1, w2, n, m): 
            # Base Case if any one of w1 or w2 is empty 
            if n == 0 or m == 0: return m or n
            
            elif w1[n-1] == w2[m-1]:
                return solve(w1, w2, n-1, m-1)
            
            else:
                return 1 + min(
                                solve(w1, w2, n-1, m-1),  # Replace
                                solve(w1, w2, n-1, m),    # Delete
                                solve(w1, w2, n, m-1)     # Insert
                                )
        
        return solve(w1, w2, len(w1), len(w2))
    
# Time Limit Exceeded
# We need to use Memoization in this Solution to avoid repetative same calculation of sub-problems



# Memoization
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dfs(i, j):
            if i == 0 or j == 0: return j or i
                        
            if (i,j) in memo:
                return memo[(i,j)]
            
            if word1[i-1] == word2[j-1]:
                ans = dfs(i-1, j-1)
            else: 
                ans = 1 + min(dfs(i, j-1), dfs(i-1, j), dfs(i-1, j-1))
                
            memo[(i,j)] = ans
            return memo[(i,j)]
        
        return dfs(len(word1), len(word2))



# Tabular DP
class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        n = len(w1); m = len(w2)
        
        dp = [[0]*(m+1) for i in range(n+1)]
        
        for j in range(m+1): # Base Case 0th row where len(w1) = 0
            dp[0][j] = j
        
        for i in range(n+1): # Base Case 0th column where len(w2) = 0
            dp[i][0] = i
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if w1[i-1] == w2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                                        dp[i-1][j-1],  # Replace 
                                        dp[i-1][j],    # Delete
                                        dp[i][j-1]     # Insert
                                        )
        
        return dp[-1][-1]
        