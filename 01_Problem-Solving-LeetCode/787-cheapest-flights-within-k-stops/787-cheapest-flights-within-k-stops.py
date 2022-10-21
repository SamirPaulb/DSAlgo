class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i:[] for i in range(n)}
        for u, v, w in flights:
            adjList[u].append((w, v))
        min_stops = [2**31] * n
        heap = [(0, src, -1)]
        while heap:
            w, v, t = heapq.heappop(heap)
            if min_stops[v] < t: continue
            if t > k: continue
            if v == dst and t <= k: return w
            min_stops[v] = t
            for w1, v1 in adjList[v]:
                if t+1 <= k:
                    heapq.heappush(heap, (w+w1, v1, t+1))
        
        return -1