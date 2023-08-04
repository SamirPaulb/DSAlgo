# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
# https://youtu.be/MOeuK6gaC2A

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        alt1, alt2 = "", ""
        
        for i in range(len(s)):
            alt1 += '1' if i%2 else '0'
            alt2 += '0' if i%2 else '1'
        
        diff1 = diff2 = 0
        for i in range(n):
            if s[i] != alt1[i]: diff1 += 1
            if s[i] != alt2[i]: diff2 += 1
        
        l = 0
        res = min(diff1, diff2)
        for r in range(n, len(s)):
            if s[r] != alt1[r]: diff1 += 1
            if s[r] != alt2[r]: diff2 += 1
            if s[l] != alt1[l]: diff1 -= 1
            if s[l] != alt2[l]: diff2 -= 1
            l += 1
            res = min(res, diff1, diff2)
        
        return res    
    
    
# Time: O(N)
# Space: O(1)
