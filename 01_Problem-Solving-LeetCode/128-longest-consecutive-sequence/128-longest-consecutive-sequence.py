class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        res = 1
        tmp = 1
        elements = set(nums)
        
        for num in nums:
            if (num - 1) in elements:
                continue
            else:
                tmp = 1
                while (num + 1) in elements:
                    tmp += 1
                    num += 1
                res = max(res, tmp)
        
        return res