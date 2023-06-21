# https://leetcode.com/problems/painting-the-walls/

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = {}
        
        def solve(i,t):
            if t >= len(time): return 0
            if i >= len(time): return 2**31
            if (i,t) in dp: return dp[(i,t)]
            ans = min(solve(i+1, t), cost[i] + solve(i+1, t+time[i]+1))
            dp[(i,t)] = ans
            return ans
        
        return solve(0,0)
    
    
# Time: O(n^2)
# Space: O(n^2)
