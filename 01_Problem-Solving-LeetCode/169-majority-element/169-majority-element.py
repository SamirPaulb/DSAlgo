class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = -1
        count = 0
        
        for num in nums:
            if num == me: count += 1
            if num != me and count > 0: count -= 1
            if count == 0: me = num; count = 1
        
        return me if nums.count(me) >= len(nums)//2 else -1