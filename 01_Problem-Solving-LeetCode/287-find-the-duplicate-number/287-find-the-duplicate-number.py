class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break
        
        pt = 0
        while True:
            slow = nums[slow]
            pt = nums[pt]
            if pt == slow: 
                return slow
        
        