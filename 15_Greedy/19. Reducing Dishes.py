# https://leetcode.com/problems/reducing-dishes/

'''
# We choose dishes from most satisfied. Everytime we add a new dish to the menu list, 
# all dishes on the menu list will be cooked one time unit later, so the result += total satisfaction on the list.
# We'll keep doing this as long as A[i] + total > 0.

class Solution:
    def maxSatisfaction(self, A: List[int]) -> int:
        n = len(A)
        A.sort()
        dp = [[-1]*(n+1) for _ in range(n+1)]
        
        def dfs(i, j):
            if i >= len(A): return 0
            if dp[i][j] != -1: return dp[i][j]
            ans = max(dfs(i+1, j), j * A[i] + dfs(i+1, j+1))
            dp[i][j] = ans
            return ans
        
        return dfs(0, 1)
    
# Time: O(N^2)
'''

class Solution:
    def maxSatisfaction(self, A: List[int]) -> int:
        res = total = 0
        A.sort()
        while A and A[-1] + total > 0:
            total += A.pop()
            res += total
        return res
      
# Time: O(N)
