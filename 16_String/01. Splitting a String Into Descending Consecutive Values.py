# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        i = 0
        while i < len(s):
            n = int(s[:i+1]) - 1
            l, r = i+1, i+1
            while r < len(s) and n >= 0:
                num = int(s[l:r+1])
                if num > n: 
                    break
                elif n == 0:
                    if int(s[l:]) == 0: return True
                    else: break
                elif num == n:
                    n -= 1
                    l = r+1
                    if l == len(s): return True
                r += 1
            i += 1
        
        return False
      
      
# Time: O(N^2)
