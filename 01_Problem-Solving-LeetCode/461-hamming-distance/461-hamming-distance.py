class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        res = 0
        
        for i in range(32):
            res += a & 1
            a = a >> 1
            
        return res