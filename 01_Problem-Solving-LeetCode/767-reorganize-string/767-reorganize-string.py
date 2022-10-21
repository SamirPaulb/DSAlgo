import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = {}
        for i in s:
            if i not in dic: dic[i] = 1
            else: dic[i] += 1
        
        maxheap = []
        for i in dic:
            maxheap.append([-dic[i], i])
        heapq.heapify(maxheap)
        
        res = ""
        while len(maxheap) > 1:
            s1 = heapq.heappop(maxheap)
            s2 = heapq.heappop(maxheap)
            
            res += s1[1]
            s1[0] += 1
            res += s2[1]
            s2[0] += 1
            
            if s1[0] <= -1: heapq.heappush(maxheap, s1)
            if s2[0] <= -1: heapq.heappush(maxheap, s2)
        
        if maxheap:
            s1 = heapq.heappop(maxheap)
            if s1[0] < -1: return ""
            else: res += s1[1]
        
        return res