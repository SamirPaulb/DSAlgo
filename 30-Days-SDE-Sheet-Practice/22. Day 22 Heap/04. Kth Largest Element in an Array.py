# https://leetcode.com/problems/kth-largest-element-in-an-array/

#------ Method 1 ----------  Using Min Heap Time: O(n log(k))
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        self.minHeap = []     # as root of min heap is minimum and root is removed in pop operation
        self.heapLength = 0   # for calculating length of heap in constant time else len() would take O(k) time
        
        def addToHeap(num):
            heapq.heappush(self.minHeap, num)
            self.heapLength += 1
            if self.heapLength > k:  # always trying to maintain heap length k 
                heapq.heappop(self.minHeap)
                self.heapLength -= 1
                
        for num in nums:        
            addToHeap(num)
        
        return self.minHeap[0]

# Time: O(N log(k))     ; O(N) for traversal and log(k) for pushing num to a heap of size k
# Space: O(k)           ; as the minHeap is always of size k


#------ Method 2 ----------  Using QUick Quick-Select (idea Quick Sort)
class Solution:
    def findKthLargest(self, nums, k):
        pivot = nums[0]
        
        left = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        
        if k <= len(right): return self.findKthLargest(right, k)
        elif len(right) < k <= len(right) + len(equal): return equal[0]
        else: return self.findKthLargest(left, k - len(right) - len(equal))

# Average Time Complexity: O(N)
# Worst Case Time Complexity: O(N^2)
# Space Complexity: O(N)
