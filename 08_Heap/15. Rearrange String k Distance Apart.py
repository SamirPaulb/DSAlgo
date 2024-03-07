# https://www.lintcode.com/problem/907

import heapq
import collections

class Solution:
    def rearrangeString(self, s, k):
        maxHeap = []
        heapq.heapify(maxHeap)
        for (ch, cnt) in collections.Counter(s).items():
            heapq.heappush(maxHeap, (-cnt, ch))

        res = ""
        while len(maxHeap) >= k:
            tmp = []
            for _ in range(k):
                cnt, ch = heapq.heappop(maxHeap)
                res += ch
                tmp.append((cnt, ch))
            for cnt, ch in tmp:
                cnt += 1
                if cnt < 0:
                    heapq.heappush(maxHeap, (cnt, ch))
        
        if len(maxHeap) > 0:
            cnt, ch = heapq.heappop(maxHeap)
            if cnt < -1: return ""
            res += ch
        
        return res 


# Time: O(len(s) * log n), where len(s) is the length of the input string and n is the number of distinct characters.
# Space: O(len(s))
