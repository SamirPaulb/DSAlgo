# https://practice.geeksforgeeks.org/problems/the-painters-partition-problem1535/1/#

# SAME AS MINIMUM NUMBER OF PAGE ALLOCATION PROBLEM using Binary Search

class Solution:
    def minTime (self, arr, n, k):
        
        def isValid(mid):
            count = 1
            s = 0
            for i in arr:
                s += i
                if s > mid:
                    count += 1
                    s = i
            return count <= k
        
        low = min(arr)
        high = sum(arr)
        while low <= high:
            mid = low + (high - low) // 2
            if isValid(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low

# the sum(arr) can at max 2^32 so max high = 2^32 
# Time: O(log(2^32) * n) = 32 * n  
# Space: O(1)
