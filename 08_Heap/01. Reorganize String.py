# https://leetcode.com/problems/reorganize-string/

import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = {}
        for  i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        maxHeap = []
        for i in dic:
            heapq.heappush(maxHeap, [- dic[i], i])
        
        ans = ""
        while len(maxHeap) > 1:
            a = heapq.heappop(maxHeap)
            b = heapq.heappop(maxHeap)
            ans += a[1]
            ans += b[1]
            # pushing a or b to maxHeap if len > 1
            if a[0] < -1: heapq.heappush(maxHeap, [a[0] + 1, a[1]])
            if b[0] < -1: heapq.heappush(maxHeap, [b[0] + 1, b[1]])
        
        if maxHeap:
            if maxHeap[0][0] < -1:
                return ""
            
            ans += maxHeap[0][1]
            
        
        return ans
            