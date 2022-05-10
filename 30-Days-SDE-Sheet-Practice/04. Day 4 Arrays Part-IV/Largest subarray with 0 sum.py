# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#
'''
Use a dictionary to store current sum if we get same sum later then it must be zero in that range.
'''

class Solution:
    def maxLen(self, n, arr):
        dic = {0:-1}
        res = 0
        s = 0
        
        for i in range(n):
            s += arr[i]
            if s in dic:
                res = max(res, i - dic[s])
            else:
                dic[s] = i
        
        return res

# Time: O(n)
# Space: O(n)