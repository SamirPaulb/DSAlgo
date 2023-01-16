# https://leetcode.com/problems/robot-bounded-in-circle/


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in 4*instructions:  # 4* for "GL"
            if i == 'G':
                x += dx
                y += dy
            elif i == 'L':
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
        
        return (x,y) == (0,0)
    
    
    
# Time: O(N)
# Space: O(1)
