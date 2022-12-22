# https://leetcode.com/problems/perfect-rectangle/

'''
Check:
1. Sum area by all small rectangles == Area by Cover or Bigger rectangle.
2. No overlapping by small rectangles.
3. No gap between the 2 rectangles.

Explanation: 
In a valid case all rectangles will share all corners exactly twice, except the four corners of the final rectangle. 
Using the set symmetric difference will remove these doubled corners and only leave the four corners of the final rectangle. 
Sum the areas of the individual rectangles and compare it to the area of the final rectangle

'''

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        X1 = Y1 = float("inf")
        X2 = Y2 = float("-inf")
        corners = set()
        area = 0
        for x1, y1, x2, y2 in rectangles:
            area += (x2-x1) * (y2-y1)
            X1 = min(X1, x1)
            Y1 = min(Y1, y1)
            X2 = max(X2, x2)
            Y2 = max(Y2, y2)
            corners ^= {(x1,y1), (x2,y2), (x1,y2), (x2,y1)}

        return area == (X2-X1) * (Y2-Y1) and corners == {(X1,Y1), (X2,Y2), (X1,Y2), (X2,Y1)}
