class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):
            # For Palindromic Substring of EVEN length
            l = i; r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                    
                l -= 1
                r += 1
                
            
            # For Palindromic Substring of ODD length
            l = i; r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                    
                l -= 1
                r += 1
                
        return res
    
# Time: O(n^2)
# Space: O(1)