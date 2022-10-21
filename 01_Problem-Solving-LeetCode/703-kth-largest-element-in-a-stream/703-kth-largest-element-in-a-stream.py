class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.len = 0
        self.minHeap = []
        for val in nums:
            self.add(val)

    def add(self, val):
        heapq.heappush(self.minHeap, val)
        self.len += 1
        if self.len > self.k: heapq.heappop(self.minHeap); self.len -= 1
        return self.minHeap[0]