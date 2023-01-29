# https://leetcode.com/problems/minimum-interval-to-include-each-query/
# https://youtu.be/5hQ5WWW5awQ

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap, i = [], 0 
        res = {} # Dictionary to retrive values as order of queries
        
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1
                
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
                
            res[q] = minHeap[0][0] if minHeap else -1
                
        return [res[q] for q in queries]
    
    
    
# Time: O(N log(N) + Qlog(Q))
