# https://leetcode.com/problems/minimum-window-substring/
# https://youtu.be/jSto0O4AJbM

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount, sWindow = {}, {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)   # if c present in tCount get its count else 0

        have = 0; need = len(tCount)
        res = ""; resLen = 2**31
        l, r = 0, 0
        while r < len(s):
            c = s[r]
            if c in tCount:
                sWindow[c] = 1 + sWindow.get(c, 0)
                if sWindow[c] == tCount[c]:
                    have += 1
            r += 1
            while have == need:
                if s[l] in sWindow:
                    if r - l < resLen:
                        res = s[l : r]
                        resLen = r - l
                    sWindow[s[l]] -= 1
                    if sWindow[s[l]] < tCount[s[l]]: 
                        have -= 1
                l += 1
        
        return res if resLen != 2**31 else ""
        
                
            
# Time: O(N)
# Space: O(N)
