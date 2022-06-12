# https://leetcode.com/problems/kth-largest-element-in-a-stream/

'''
By default Min Heap is implemented by heapq library.
In a Min-Heap the minimum element present at the root. In pop operation root node is removed.

'''

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []  # Min Heap
        for num in nums:
            heapq.heappush(self.minHeap, num)   # adding all elements to min heap
            
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)   # Only keeping k maximum elements
        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # first add to min heap
        
        if len(self.minHeap) > self.k:    # if length greater pop minimum element as root is the min
            heapq.heappop(self.minHeap)
            
        return self.minHeap[0]            # root is minHeap[0] as root is k'th max
    
# Time: O(N log(N))     # as heap size is N so heappush takes log(N) time
# Space: O(N)
    
    
    
# Method-2  Using the given add function to add only k elements so that we can save space
import heapq
class KthLargest:
    """
    The idea is to ALWAYS maintain a MIN heap with only K elements
    - in this case, the K-the largest element (in the stream)
    - will always be at the root position
    """
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for num in nums:
            self.add(num) # add elements using the function below
        
    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        
        # if after adding the new item causes 
        # the heap size to increase beyond k, 
        # then pop out the smallest element 
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)
            
        return self.heap[0] # the root element
    
# Time: O(N log(K))  # as heap size if k so heappush takes log(k) time
# Space: O(K)        # as only making heap of size k

