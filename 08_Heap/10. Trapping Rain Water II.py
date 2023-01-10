# https://leetcode.com/problems/trapping-rain-water-ii/
# https://youtu.be/QvQiQcLCQ4Y

import heapq
class Solution:
    def trapRainWater(self, heightMap):
        minHeap = []
        ROW, COL = len(heightMap), len(heightMap[0])
        visited = [[False]*COL for _ in range(ROW)]
        
        for i in range(ROW):
            for j in range(COL):
                if i in (0, ROW-1) or j in (0, COL-1):
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        res = 0
        minBdH = 0  # Minimum Boundary Height
        while minHeap:
            h, i, j = heapq.heappop(minHeap)
            minBdH = max(minBdH, h)
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                r, c = i+dx, j+dy
                if 0<=r<ROW and 0<=c<COL and not visited[r][c]:
                    visited[r][c] = True
                    heapq.heappush(minHeap, (heightMap[r][c], r, c))
                    if heightMap[r][c] < minBdH:
                        res += minBdH - heightMap[r][c]
        
        return res
    
    
    
# Time: O(m*n * log(m*n))
# Space: O(m*n)
