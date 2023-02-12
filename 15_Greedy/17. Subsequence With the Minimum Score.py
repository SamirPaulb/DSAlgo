# https://leetcode.com/problems/subsequence-with-the-minimum-score/

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        # Take care of the case where t is already a substring of s, return 0 in this case.
        j = 0
        for i in range(len(s)):
            if s[i]==t[j]: j+=1
            if j==len(t): return 0
        
        # Moving forward, store the first letter's index in t that needs to be removed if s ends at i.
        firstRemovedIndexFromLeft = [0]*len(s)
        left = 0
        for i in range(len(s)):
            if s[i]==t[left]:
                left += 1
            firstRemovedIndexFromLeft[i] = left
        print(firstRemovedIndexFromLeft)
        # Worest case, we remove the first and last letter in t.
        res = len(t)
        
        # Moving backward, at each position i in s, there are two cases:
        # (1) the firstRemovedIndexFromLeft[i] <= first removed index from right,
        #       This is a valid case in the sense that we can 
        #       basically, remove everything in between these two indices, including these two indices.
        #       i.e.,
        #       s = 'aabbbaa'
        #       t = 'aazzzaa'
        #       firstRemovedIndexFromLeft  = [1, 2, 2, 2, 2, 2, 2]
        #       firstRemovedIndexFromRight = [4, 4, 4, 4 ,4, 5, 6] (We don't actually put the right in arr like this, but just for easy understanding here)
        #       when i=3, firstRemovedIndexFromLeft[i] = 2 and right = 4, 
        #       so we try to update res, if the score (right-left+1) is smaller.
        #
        # (2) left > right, this is an invalid case to consider both indices.
        #       In this case, we basically just remove everything from 0 to index right, 
        #       score is (right - 0 + 1), where 0 is the left index. Update res if score is smaller.
        right = len(t) -1 
        for i in reversed(range(len(s))):
            if right>=firstRemovedIndexFromLeft[i]:
                res = min(right-firstRemovedIndexFromLeft[i]+1,res)
            if s[i] == t[right]:
                right -= 1
            res = min(res, right+1)
            
        return res
