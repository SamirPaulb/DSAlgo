# https://leetcode.com/problems/trapping-rain-water/


'''
Find left and right boundary for the current element the keep addding the amount of
water above the current height to the result. 
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0; r = len(height)-1
        res = 0
        leftMax = height[0]
        rightMax = height[-1]
        
        while l <= r:
            if height[l] <= height[r]:
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l] 
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                r -= 1
        
        return res
    
# Time: O(N)
# Space: O(1)




# Method - 2
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftBoundary, rightBoundary = [0] * n, [0] * n 
        lMax, rMax, ans = height[0], height[-1], 0
        
        for i in range(n):
            lMax = max(lMax, height[i])
            leftBoundary[i] = lMax
        
        for i in range(n - 1, -1, -1):
            rMax = max(rMax, height[i])
            rightBoundary[i] = rMax
        
        for i in range(n):
            ans += min(leftBoundary[i], rightBoundary[i]) - height[i]
        
        return ans
    
# Time: O(N)
# Space: O(N)