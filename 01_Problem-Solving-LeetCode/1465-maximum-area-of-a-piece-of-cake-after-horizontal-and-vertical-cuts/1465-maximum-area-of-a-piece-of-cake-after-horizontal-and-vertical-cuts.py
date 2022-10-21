class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hc = sorted(horizontalCuts)
        vc = sorted(verticalCuts)
        
        max_h = max(hc[0], h - hc[-1])
        for i in range(1, len(hc)):
            max_h = max(max_h, hc[i] - hc[i-1])
        
        max_c = max(vc[0], w - vc[-1])
        for i in range(1, len(vc)):
            max_c = max(max_c, vc[i] - vc[i-1])
        
        return (max_h * max_c) % (10**9 + 7)