# https://leetcode.com/problems/largest-sum-of-averages/

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp = [[-1] * (k+1) for i in range(len(nums))]
        
        def dfs(i, k):      # Time: O(N * K)
            if i >= len(nums) or k < 0: return 0
            if k == 0: return -2**31
            if dp[i][k] != -1: return dp[i][k]
            ans = 0
            s = 0
            for j in range(i, len(nums)):   # Time: O(N)
                s += nums[j]
                ans = max(ans, s/(j-i+1) + dfs(j+1, k-1))
            dp[i][k] = ans
            return ans
        
        return dfs(0, k)
    

'''
Time: O(K * N * N)
Space: O(K * N * N)
'''
