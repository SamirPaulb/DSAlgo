# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
# Function to find a continuous sub-array which adds up to a given number.

class Solution:
    def subArraySum(self,arr, n, s): 
        curSum = 0
        l = 0
        for r in range(n):
            curSum += arr[r]
            while curSum > s and l < r:
                curSum -= arr[l]
                l += 1
            if curSum == s: return [l+1, r+1]
        
        
       
       
       
       
 