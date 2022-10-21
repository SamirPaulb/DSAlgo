class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0; r = len(height)-1
        res = 0
        
        while l < r:
            h = min(height[l], height[r]) 
            w = r - l
            area = h * w
            res = max(res, area)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return res