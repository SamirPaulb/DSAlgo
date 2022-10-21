class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        
        me1 = ""
        me2 = ""
        count1 = 0
        count2 = 0
        
        for num in nums:
            if me1 == num:
                count1 += 1
            elif me2 == num:
                count2 += 1
            elif count1 == 0:
                me1 = num
                count1 = 1
            elif count2 == 0:
                me2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        if nums.count(me1) > len(nums)//3: res.add(me1)
        if nums.count(me2) > len(nums)//3: res.add(me2)
        
        return res