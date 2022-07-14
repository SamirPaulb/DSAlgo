# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        for i in range(32):
            if (a & 1) | (b & 1) != (c & 1):
                if (c & 1) == 1:  # (a & 1) | (b & 1) should be == 1 ; so changing any of a, b we can get 1
                    res += 1      
                else:             # (a & 1) | (b & 1) should be == 0 ; is (a & 1) == 1 and (b & 1) == 1 we need to change both to 0 so res += 1; if any of them is 1 then change only 1 i.e. res += 1
                    res += (a & 1) + (b & 1) 
            a, b, c = a>>1, b>>1, c>>1   # left-shift by 1
        
        return res
      
# Time: O(1)
# Space: O(1)
