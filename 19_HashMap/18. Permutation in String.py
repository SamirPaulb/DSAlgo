# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1, s2):
        k = len(s1)
        s1d = collections.Counter(s1)
        s2d = collections.Counter(s2[:k])
        if s1d == s2d: return True
        for i in range(k, len(s2)):
            s2d[s2[i]] += 1
            s2d[s2[i-k]] -= 1
            if s1d == s2d: return True
        
        return False
    
    
# Time: O(N); where N = len(s2)
# Space: O(K)
