# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# https://youtu.be/-qrpJykY2gE

'''
# Intuition:
Traverse from LSB to MSB and keep right-shifting left and right until both of them become equal. 
If at any bit position left side bits of left and right are equal ie. left == right, 
then all numbers in [left, right] will also be equal.

e.g.
bit index =  3 2 1 0
left =  12 = 1 1 0 0
        13 = 1 1 0 1
        14 = 1 1 1 0
right = 15 = 1 1 1 1

After right-shifting left and right 2 times(ie. count = 2), left == right = 12 = 13 = 14 = 15 = 0 0 1 1
So '&' of all number in [left, right] is (left << count)
'''


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        
        while left != right:
            left = left >> 1
            right = right >> 1
            count += 1
        
        return left << count
                
         
# Time: O(1)
# Space: O(1)
