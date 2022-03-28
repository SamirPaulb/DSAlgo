# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Note:  *There will be only two majority element*. suppose there are 3 majority element then count of each element will be n/3 and there will be only there 3 unique elements in the array. But question is elements that appear *more than ⌊ n/3 ⌋ times*.
        n = len(nums)
        me1 = -1    # Majority element 1
        me2 = -2    # Majority element 2
        count1 = 0  # Count of Majority element 1
        count2 = 0  # Count of Majority element 2
        
        for num in nums:
            if num == me1: count1 += 1

            elif num == me2: count2 += 1

            elif count1 == 0: me1 = num; count1 = 1
                                
            elif count2 == 0: me2 = num; count2 = 1
                
            else:
                count1 -= 1
                count2 -= 1
        
        res = set()  # taking set instead of list as me1 and me2 can be equal
        if nums.count(me1) > n // 3: res.add(me1)
        if nums.count(me2) > n // 3: res.add(me2)
        
        return res