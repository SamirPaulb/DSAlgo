# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        
        leftBoundary = [0]*n # Nearest Smaller to Left
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                leftBoundary[i] = 0
            else:
                leftBoundary[i] = stack[-1] + 1
            stack.append(i)
        
        rightBoundary = [n-1]*n # Next Smaller to Right
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                rightBoundary[i] = n-1
            else:
                rightBoundary[i] = stack[-1] - 1
            stack.append(i)
        
        res = 0
        for i in range(n):
            width = rightBoundary[i] - leftBoundary[i] + 1
            height = heights[i]
            area = height * width
            res = max(res, area)
        
        return res
            
            