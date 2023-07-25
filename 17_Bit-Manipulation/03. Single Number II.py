# https://leetcode.com/problems/single-number-ii/
# Explanation: https://spcdn.pages.dev/single-number-ii.pdf

class Solution:
    def singleNumber(self, nums):
        res = 0
        negCount = 0
        for i in range(32):
            s = 0
            for num in nums:
                if num < 0: 
                    negCount += 1
                if (abs(num) >> i) & 1:
                    s += 1
                    s %= 3
            res |= (s << i)

        return -res if negCount%3 else res




        

class Solution:
    # Optimal best approach
    def singleNumber(self, nums):
        ones = 0; twos = 0
        for num in nums:
            ones = (ones ^ num) & (~twos)
            twos = (twos ^ num) & (~ones)
        return ones
        # Time: O(N)
        # Space: O(1)
    
    
    def singleNumber1(self, nums):
        nums.sort()
        if nums[0] != nums[1]: return nums[0]
        if nums[-1] != nums[-2]: return nums[-1]
        i = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                return nums[i-1]
            i += 3
        # Time Complexity = O(N log(N)) 
        # as nums[i] < 2**31 so in worst case Time = O(N log(2**31)) = O(31 * N)
        # This approach is faster than O(32N) because in normal senario it uses less time than 32N
        # Space: O(1) ; as sorting the given array not taking any extra array   
            
            
    def singleNumber2(self, nums):
        return (3*sum(set(nums)) - sum(nums)) // 2
        # Time: O(N) ; as sum() function internally uses loop
        # Space: O(N); for making the set of nums
