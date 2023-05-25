# https://leetcode.com/problems/path-with-minimum-effort/
# https://youtu.be/FabSLaGu0NI

# Method 1  --------> using Dijkstra's Algorithm
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        visited = set()
        minHeap = [(0,0,0)]  # (distance, row, col)
        while minHeap:
            h,r,c = heapq.heappop(minHeap)
            if (r,c) == (row-1, col-1): return h
            if (r,c) in visited: continue
            visited.add((r,c))
            for x,y in ((0,1),(0,-1),(1,0),(-1,0)):
                nr, nc = r+x, c+y
                if not (0<=nr<row and 0<=nc<col): continue
                nh = max(h, abs(heights[nr][nc] - heights[r][c]))
                heapq.heappush(minHeap, (nh,nr,nc))
        
        return 0

# Time: O(r*c * log(r*c))
# Space: O(r * c)


'''
# Method 2  --------> using Binary Search
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
    
    
'''
