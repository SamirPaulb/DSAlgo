# https://leetcode.com/problems/maximum-star-sum-of-a-graph/

import heapq
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adjList = {i:[] for i in range(len(vals))}
        
        for a, b in edges:
            if vals[b] > 0: 
                heapq.heappush(adjList[a], vals[b])
                if len(adjList[a]) > k:
                    heapq.heappop(adjList[a])
            if vals[a] > 0:
                heapq.heappush(adjList[b], vals[a])
                if len(adjList[b]) > k:
                    heapq.heappop(adjList[b])
                    
        res = -2**31
        for i in range(len(vals)):
            tmp = vals[i]
            tmp += sum(adjList[i])
            res = max(res, tmp)
            
        return res
    
    
# Time: O(N + E * log(K))
# Space: O(N*K)
