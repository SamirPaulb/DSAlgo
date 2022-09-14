# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://youtu.be/qtVh-XEpsJo

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in track:
                track.remove(s[l])
                l += 1                
            res = max(res, r-l+1)
            track.add(s[r])
        
        return res

# Time Complexity: O(N)   
# Space Complexity: O(len(set(s)))  # number of unique charecters
