# https://leetcode.com/problems/path-with-minimum-effort/

# https://youtu.be/FabSLaGu0NI

# Method 1  --------> using Dijkstra's Algorithm
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        
        minHeap = []
        heapq.heappush(minHeap, (0, 0, 0))  # (distance, row, col)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        dp = [[2**31]*col for i in range(row)]
        
        while minHeap:
            d, r, c = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r,c))
            dp[r][c] = d
            if r == row-1 and c == col-1: return dp[r][c]    
            for direc in directions:
                nr = r + direc[0]
                nc = c + direc[1]
                if 0 <= nr < row and 0 <= nc < col:
                    nd = max(dp[r][c], abs(heights[r][c] - heights[nr][nc]))
                    if nd < dp[nr][nc]:
                        heapq.heappush(minHeap, (nd, nr, nc))
        
        return 0

# Time: O(r*c * log(r*c))
# Space: O(r * c)


'''
# Method 2  --------> using Binary Search
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
    
    
'''
