# https://leetcode.com/problems/single-number-iii/
# https://www.youtube.com/watch?v=faoVORjd-T8

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor = xor ^ num
        
        diff_bit = 1
        while not (xor & diff_bit):
            diff_bit = diff_bit << 1
        
        xorGroupA = xorGroupB = 0
        for num in nums:
            if num & diff_bit:
                xorGroupA = xorGroupA ^ num
            else:
                xorGroupB = xorGroupB ^ num
        
        return [xorGroupA, xorGroupB]