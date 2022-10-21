class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0; r = len(s)-1
        lPal = True
        count = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if count == 1:
                    lPal = False
                    break
                l += 1
                count += 1
        
        l = 0; r = len(s)-1
        rPal = True
        count = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if count == 1:
                    rPal = False
                    break
                r -= 1
                count += 1
        
        return lPal or rPal
    