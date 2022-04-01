# https://leetcode.com/problems/find-median-from-data-stream/
# https://youtu.be/itmhHWaHupI

# we can easyly solve using arr operations in O(N) time but to solve in log(N) time we have to use heap
# using 2 heaps one is left side of median ig. self.small(maxheap) and another is right side of median self.large(minheap)

import heapq
class MedianFinder:

    def __init__(self):
        self.small = []   # Max Heap
        self.large = []   # Min Heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)  # always pushing on small (maxheap) then comparing
        
        if self.small and self.large and -self.small[0] > self.large[0]: # if newly added element greater
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1: 
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-self.small[0] + self.large[0]) / 2
        
# Time: O(log(N))
# Space: O(N)
