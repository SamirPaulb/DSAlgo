class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0; r = len(height)-1
        res = 0
        lMax = height[0]
        rMax = height[r]
        
        while l < r:
            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])
            
            if height[l] < height[r]:
                res += min(lMax, rMax) - height[l]
                l += 1
            else:
                res += min(lMax, rMax) - height[r]
                r -= 1
        
        return res