import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st = [-i for i in stones]
        heapq.heapify(st)
        while len(st) > 1:
            a = -heapq.heappop(st)
            b = -heapq.heappop(st)
            heapq.heappush(st, -(a-b))
        
        return -st[0]