# https://leetcode.com/problems/ugly-number
# https://youtu.be/M0Zay1Qr9ws

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n = n // p
                
        return n == 1
