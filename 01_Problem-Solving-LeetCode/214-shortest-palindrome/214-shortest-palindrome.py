class Solution:
    def shortestPalindrome(self, s: str) -> str:
        m = len(s)-1
        for i in range(len(s)-1, -1, -1):
            if s[:i+1] == s[:i+1][::-1]:
                m = i
                break
        
        return s[m+1:][::-1] + s