class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ''' Brute Force
        n = len(arr)
        res = 0
        
        for i in range(n):
            mini = arr[i]
            for j in range(i, n):
                mini = min(mini, arr[j])
                res += mini
        
        return res % (10**9 + 7)
    
# Time: O(n^2)
# Space: O(1)
'''
        # Optimal approach => similar to Rain Water Trap problem
        # make left boundary => it defines number of left subarrays in which the current element is minimum
        lb = []; stack = [] # (cur, curCount)
        for cur in arr:
            curCount = 1
            while stack and stack[-1][0] > cur:
                peak = stack.pop()
                curCount += peak[1]
            stack.append((cur, curCount))
            lb.append(curCount)
        
        # make right boundary => it defiens number of right subarrays in which the current element if minimum
        rb = []
        stack = []
        for cur in arr[::-1]:
            curCount = 1
            while stack and stack[-1][0] >= cur:
                peak = stack.pop()
                curCount += peak[1]
            stack.append((cur, curCount))
            rb.append(curCount)
        rb.reverse()
        res = 0
        for i in range(len(arr)):
            res += arr[i] * lb[i] * rb[i]
        
        return res % (10**9 + 7)