# https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle2948/1
# https://youtu.be/yCQN096CwWM

class Solution:
    def maximumSumRectangle(self,R,C,M):
        
        def kadanes(arr):
            cs = 0
            ms = arr[0]
            for a in arr:
                cs += a
                cs = max(cs, a)
                ms = max(ms, cs)
            return ms
        
        res = kadanes(M[0])
        for i in range(R):
            arr = [0] * C
            for r in range(i, R):
                for c in range(C):
                    arr[c] += M[r][c]
                res = max(res, kadanes(arr))
        
        return res
        
        
# Time Complexity: O(R * R * C)
# Auxiliary Space: O(C)
