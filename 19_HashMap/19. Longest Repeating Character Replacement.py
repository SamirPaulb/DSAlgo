# https://leetcode.com/problems/longest-repeating-character-replacement/

'''Intuition:
- Scan the array with 2 pointers: left and right
- Store the frequency of each character
- Compute the replacement cost: cells count between left and right pointers - the highest frequency
- if the replacement cost <= k: update longest string size
- if the replacement cost > k: decrease frequency of character at left pointer; increase left pointer and repeat
'''

class Solution:
    def characterReplacement(self, s, k):
        maxFreq = 1
        freq = collections.Counter()
        res = 1
        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])
            cost = (r-l+1) - maxFreq
            if cost <= k:
                res = max(res, r-l+1)
            else:
                freq[s[l]] -= 1
                l += 1
        
        return res
    
    
    
# Time: O(N)
# Space: O(N)
