import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            d = -(p[0]**2 + p[1]**2)
            heapq.heappush(heap, (d, p))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
# Time: O(N log(k))
# Space: O(N)