# https://leetcode.com/problems/maximum-performance-of-a-team/
# https://youtu.be/Y7UTvogADH0

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = [(e, s) for e, s in zip(efficiency, speed)]
        eng.sort(reverse = True)
        
        minHeap, spd, res = [], 0, 0
        for e, s in eng:
            if len(minHeap) == k: 
                spd -= heapq.heappop(minHeap)
            spd += s
            res = max(res, spd * e)
            heapq.heappush(minHeap, s)
        
        return res % 1000000007
    
    
# Time: O(N log(N))
