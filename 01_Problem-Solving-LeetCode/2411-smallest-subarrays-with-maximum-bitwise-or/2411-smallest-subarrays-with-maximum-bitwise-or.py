class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lastIndex = [0] * 32
        res = [1] * n
        
        for i in range(n-1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    lastIndex[j] = i
            # print(lastIndex)
            res[i] = max(1, max(lastIndex) - i + 1)
        
        return res