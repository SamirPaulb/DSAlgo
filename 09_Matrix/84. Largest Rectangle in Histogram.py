class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Finding Left Boundary
        stack = []
        lb = []  # Left Boundary
        for i in range(len(heights)):
            while stack:
                if heights[stack[-1]] >= heights[i]:
                    stack.pop()
                else:
                    lb.append(stack[-1] + 1)
                    stack.append(i)
                    break
            if len(stack) == 0:
                stack.append(i)
                lb.append(0)
        # Finding Right Boundary
        stack = []
        rb = []
        for i in range(len(heights)-1, -1, -1):
            while stack:
                if heights[stack[-1]] >= heights[i]:
                    stack.pop()
                else:
                    rb.append(stack[-1] - 1)
                    stack.append(i)
                    break
            if len(stack) == 0:
                stack.append(i)
                rb.append(len(heights) - 1)
        rb = rb[::-1]
        
        maxArea = 0
        for i in range(len(heights)):
            weight = abs(lb[i] - rb[i]) + 1
            height = heights[i]
            maxArea = max(maxArea, weight * height)
        
        return maxArea