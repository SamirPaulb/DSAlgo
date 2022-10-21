class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights); col = len(heights[0])
        visited = [[False]*col for i in range(row)]
        
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minheap = [(0, 0, 0)] # dist, row, col
        while minheap:
            eff, i, j = heapq.heappop(minheap)
            if visited[i][j]: continue
            visited[i][j] = True
            if i == row-1 and j == col-1: return eff
            for m in moves:
                r = i + m[0]; c = j + m[1]
                if 0 <= r < row and 0 <= c < col and not visited[r][c]:
                    diff = max(eff, abs(heights[r][c] - heights[i][j]))
                    heapq.heappush(minheap, (diff, r, c))
        