class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = {i:0 for i in range(min(nums)-k, max(nums)+k+1)}
        count = 0
        for i in nums:
            count += seen[i-k] + seen[i+k]
            seen[i] += 1
        
        return count