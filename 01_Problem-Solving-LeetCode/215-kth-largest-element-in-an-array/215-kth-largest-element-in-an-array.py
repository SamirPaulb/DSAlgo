import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        heapq.heapify(nums)
        while nums:
            if k == 0: return heapq.heappop(nums)
            k -= 1
            heapq.heappop(nums)