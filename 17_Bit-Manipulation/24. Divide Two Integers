# https://leetcode.com/problems/divide-two-integers/description/
# https://www.youtube.com/watch?v=pBD4B1tzgVc

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        n = abs(dividend)
        d = abs(divisor)
        res = 0
        while n >= d:
            t = 0
            while n >= (d << (t+1)):
                t += 1
                
            res += 1 << t
            n -= d << t
        
        return -res if (dividend < 0) ^ (divisor < 0) else res 


# Time: O(log N)
# Space: O(1)
