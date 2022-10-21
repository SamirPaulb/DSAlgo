import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        for i in range(k):
            a = heapq.heappop(nums)
            a *= -1
            heapq.heappush(nums, a)
        
        return sum(nums)