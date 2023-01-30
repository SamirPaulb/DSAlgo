# https://leetcode.com/problems/two-city-scheduling/
# https://youtu.be/d-B_gk_gJtQ

# ------------------ Greedy Solution ------------------
class Solution:
    def twoCitySchedCost(self, costs):
        diffs = []
        for ac, bc in costs:
            diffs.append((bc-ac, ac, bc))
        diffs.sort()
        res = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                res += diffs[i][2]    # sending to city B     
            else:
                res += diffs[i][1]    # sending to city A
        return res

# Time: O(n log(n))

# ------------------ Dynamic Programming ------------------
class Solution:
    def twoCitySchedCost(self, costs):
        n = len(costs)//2
        dp = [[-1]*(n+1) for _ in range(n+1)]
        
        def dfs(i, a, b):
            if a == b == n:
                return 0
            if i >= len(costs) or a > n or b > n:
                return 2**31
            if dp[a][b] != -1:
                return dp[a][b]
            
            aCost = costs[i][0] + dfs(i+1, a+1, b)
            bCost = costs[i][1] + dfs(i+1, a, b+1)
            
            dp[a][b] = min(aCost, bCost)
            return dp[a][b]
        
        return dfs(0, 0, 0)
    
    
# Time: O(n^2)
