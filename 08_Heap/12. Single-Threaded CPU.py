# https://leetcode.com/problems/single-threaded-cpu/
# https://youtu.be/RR1n-d4oYqE

import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda x:x[0])
        
        res, minHeap = [], []
        i, time = 0, tasks[0][0]
        
        while i < len(tasks) or minHeap:
            while i < len(tasks) and time >= tasks[i][0] :
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            if not minHeap:
                time = tasks[i][0]
            else:
                procTime, indx = heapq.heappop(minHeap)
                res.append(indx)
                time += procTime
        
        return res
    
    
# Time: O(N)
# Space: O(N)
