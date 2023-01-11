# https://leetcode.com/problems/get-equal-substrings-within-budget/
'''
Calculate the differences between a[i] and b[i].
Use a sliding window to track the longest valid substring.
'''

class Solution:
    def equalSubstring(self, s, t, maxCost):
        costs = []
        for i in range(len(s)):
            costs.append(abs(ord(s[i]) - ord(t[i])))
        
        curCost = res = l = 0
        for r in range(len(s)):
            curCost += costs[r]
            if curCost <= maxCost:
                res = max(res, r-l+1)
            else:
                curCost -= costs[l]
                l += 1
        
        return res
    
    
# Time: O(N)
