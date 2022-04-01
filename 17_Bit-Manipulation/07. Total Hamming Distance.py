# https://leetcode.com/problems/total-hamming-distance/
'''
Notice the total hamming distance is the sum of the total hamming distance for each of the i-th bits separately.

Total hamming distance for the i-th bit = 
(the number of zeros in the i-th position) * (the number of ones in the i-th position).

We then add all of these together to get our answer.
'''

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(32):
            mask = 1 << i      # left shifting 1 by i eg. 1 << 4 = 00010000
            zero = 0; one = 0  # count of 0 and 1 at i'th bit position for all elements of nums
            for num in nums:
                if num & mask: # if 1
                    one += 1   
                else:          # if 0
                    zero += 1
            
            res += zero * one  # total number of diff bits at i'th position
        
        return res

# Time: O(N) ; where N = len(nums)
# Space: O(1); not using any extra data structure