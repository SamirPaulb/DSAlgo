# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n&(1<<i):
                res |= (1<<(31-i))
        return res
