# https://leetcode.com/problems/number-of-1-bits/
# https://youtu.be/5Km3utixwZs

class Solution:
    def hammingWeight(self, n: int) -> int:
        
# ------ Methode 1 --------------------
        res = 0
        for i in range(32):
            res += n & 1
            n = n >> 1
        
        return res

# ------ Methode 2 --------------------
        res = 0
        for i in range(32):
            res += n%2
            n = n >> 2
        
        return res

# ------ Methode 3 --------------------
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        
        return res



    