# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcnt = collections.Counter(t)
        scnt = collections.Counter()
        stMatch = collections.Counter()
        res = ""
        l = 0
        res = ""
        maxLen = len(s)
        
        for r in range(len(s)):
            if s[r] in tcnt:
                scnt[s[r]] += 1
                if scnt[s[r]] >= tcnt[s[r]]:
                    stMatch[s[r]] = tcnt[s[r]]
            # print(stMatch)
            while stMatch == tcnt and l <= r:
                if r-l+1 <= maxLen:
                    maxLen = r-l+1
                    res = s[l:r+1]
                if s[l] in tcnt: 
                    scnt[s[l]] -= 1
                    if scnt[s[l]] < tcnt[s[l]]:
                        stMatch[s[l]] = scnt[s[l]]
                l += 1
            # print(l,r,scnt)
        return res
        
                
            
# Time: O(N)
# Space: O(N)
