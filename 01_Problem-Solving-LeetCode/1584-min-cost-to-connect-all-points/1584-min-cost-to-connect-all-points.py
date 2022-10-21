class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = {i:[] for i in range(n)}
        for i in range(n):
            x1 = points[i][0]; y1 = points[i][1]
            for j in range(n):
                x2 = points[j][0]; y2 = points[j][1]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        res = 0
        visited = set()
        minHeap = [(0, 0)]
        while len(visited) < n:
            dist, point = heapq.heappop(minHeap)
            if point in visited: continue
            visited.add(point)
            res += dist
            for d, p in adjList[point]:
                if p not in visited:
                    heapq.heappush(minHeap, (d, p))
        
        return res