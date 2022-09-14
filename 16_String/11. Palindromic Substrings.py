# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        def getPalCounts(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        res = 0
        for i in range(len(s)):
            res += getPalCounts(i, i)    # for palindromes of odd length
            res += getPalCounts(i, i+1)  # for palindromes of even length
        
        return res
    
    
# Time: O(N^2)
# Space: O(1)
