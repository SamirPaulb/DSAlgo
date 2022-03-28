# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        # https://en.wikipedia.org/wiki/Digital_root
        #  In base 10, this is equivalent to taking the remainder upon division by 9 (except when the digital root is 9, where the remainder upon division by 9 will be 0).
        if num == 0: return 0
        
        elif num % 9 == 0: 
            return 9
        
        else:
            return num % 9

