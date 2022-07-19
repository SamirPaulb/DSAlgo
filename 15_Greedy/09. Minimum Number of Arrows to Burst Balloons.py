# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
'''
Approch:
1. Sort the points by the end
2. Put an arrow at the end of the 1-st points
3. From the 2-nd points, we check whether the current arrow pass through the current points, if not add an arrow, put it at the end of the current points

'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        res = 0
        arrow = 0
        for start, end in points:
            if res == 0 or start > arrow:
                res += 1
                arrow = end
        
        return res
    
    
