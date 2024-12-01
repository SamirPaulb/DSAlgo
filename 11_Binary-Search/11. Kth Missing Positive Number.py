# https://leetcode.com/problems/kth-missing-positive-number/
# https://www.youtube.com/watch?v=uZ0N_hZpyps

# Brute Force approach
# If there were no elements in arr, then Kth element would be k.
# But for every element of value less than equal to k, will make
# Kth missing value shift to right 
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in arr:
            if i <= k: k += 1 
            else: break
        return k
# Time: O(N)
# Space: O(1)


# Binary Search approach => Most Optimised
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l,r = 0,len(arr)-1
        while l<=r:
            m = l+(r-l)//2
            tmp = m
            if arr[m] - m - 1 < k:
                l = m+1
            else:
                r = m-1
        # Now r<l and arr[r] to arr[l]: Kth element is in this window
        return arr[r] + (k - (arr[r]-r-1))

# Time: O(log(N))
# Space: O(1)
