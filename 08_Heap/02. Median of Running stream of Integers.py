# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=547645422524434&ppid=454615229006519&practice_plan=0
# https://practice.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1
# https://www.interviewbit.com/blog/find-median-in-a-stream/


class Solution:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def balanceHeaps(self):
        #Balance the two heaps size , such that difference is not more than one.
        if self.min_heap and self.max_heap and - self.min_heap[0] > self.max_heap[0]:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def getMedian(self):
        # return the median of the data received till now.
        if len(self.min_heap) > len(self.max_heap):
            return -self.min_heap[0]
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        else:
            return (-self.min_heap[0] + self.max_heap[0]) // 2

    def insertHeaps(self,x):
        heapq.heappush(self.min_heap, -x)
        self.balanceHeaps()
            


