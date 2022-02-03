# https://leetcode.com/problems/jump-game-ii/

# ----------------------  Dynamic Programming Approach => TLE  ---------------------------------
# https://youtu.be/cETfFsSTGJI
class Solution:
    def jump(self, nums):
        n = len(nums)
        dp = [0]*n
        
        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:          # check if we can directly reach i from j
                    if dp[i] == 0:            # previously no one has reached i 
                        dp[i] = dp[j] + 1     # update
                    else:
                        if dp[j] + 1 < dp[i]: # update only if current jumps is lesser
                            dp[i] = dp[j] + 1
        
        return dp[-1]
    
# Time: O(n^2)
# Space: O(n)
# We can also find the path of min jumps if we store the j index during updating dp in another array
# then traverse from n-1 to 0 to find the path of min jumps 


# ----------------------  Greedy Approach => All Testcases Passed  --------------------------------
# https://www.youtube.com/watch?v=dJ7sWiOoK7g
class Solution:
    def jump(self, nums):
        l = 0
        r = 0
        res = 0
        
        while r < len(nums) - 1:
            maxReachableIndex = 0
            for i in range(l, r+1):
                maxReachableIndex = max(maxReachableIndex, i + nums[i])
            
            l = r + 1
            r = maxReachableIndex
            res += 1
        
        return res
    
# Time Complexity: O(N); as the inner for loop is also increasing r so intotal one loop
# Space Complexity: O(1)