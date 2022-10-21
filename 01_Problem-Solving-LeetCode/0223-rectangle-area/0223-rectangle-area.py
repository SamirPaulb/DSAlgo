class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a_area = abs(ax1 - ax2) * abs(ay1 - ay2)
        b_area = abs(bx1 - bx2) * abs(by1 - by2)
        
        if (bx1 < ax2 and ax1 < bx2) and (by1 < ay2 and ay1 < by2): # Intersection
            rx1 = max(ax1, bx1)
            rx2 = min(ax2, bx2)
            ry1 = max(ay1, by1)
            ry2 = min(ay2, by2)
            return a_area + b_area - abs(rx1 - rx2) * abs(ry1 - ry2)
        
        return a_area + b_area  # No Intersection
            
        