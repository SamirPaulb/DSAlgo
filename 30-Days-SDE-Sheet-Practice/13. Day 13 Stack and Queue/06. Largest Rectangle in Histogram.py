# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # left boundary => next smaller element to left
        stack = []
        nextSmallerLeft = [0]*n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nextSmallerLeft[i] = stack[-1] + 1
            stack.append(i)
        
        # right boundary => next smaller element to right
        stack = []
        nextSmallerRight = [n-1]*n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nextSmallerRight[i] = stack[-1] - 1
            stack.append(i)
        
        res = heights[0]
        for i in range(n):
            height = heights[i]
            weidth = nextSmallerRight[i] - nextSmallerLeft[i] + 1
            area = height * weidth
            res = max(res, area)
            
        return res

# Time: O(N)
# Space: O(N)