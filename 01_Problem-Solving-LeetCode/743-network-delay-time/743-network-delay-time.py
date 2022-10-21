class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i:[] for i in range(n+1)}
        for u, v, w in times:
            adjList[u].append((v, w))
        
        res = 0
        visited = set()
        minHeap = [(0, k)]
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited: continue
            visited.add(node)
            res = max(res, time)
            for v, w in adjList[node]:
                if v not in visited:
                    heapq.heappush(minHeap, (time + w, v))
        
        return res if len(visited) == n else -1