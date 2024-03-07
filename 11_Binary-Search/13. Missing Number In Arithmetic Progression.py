# https://www.lintcode.com/problem/3633

from typing import List

########################### Solution 1 -> Binary Search ###########################
class Solution:
    def missing_number(self, arr: List[int]) -> int:
        # An = A0 + (n-1) * d 
        n = len(arr)+1
        d = (arr[-1] - arr[0]) // (n-1)
        l, r = 0, n-2
        while l <= r:
            m = l + (r-l)//2
            nl = m+1
            nr = n-m-1
            if abs(arr[m] - arr[0]) // abs(d) + 1 > nl :
                if m != 0 and arr[m-1] != arr[m] - d: return arr[m] - d 
                r = m - 1
            else:
                if m != n-1 and arr[m+1] != arr[m] + d: return arr[m] + d 
                l = m + 1

        return -1

# Time: O(log(n))
# Space: O(1)


########################### Solution 2 -> Math ###########################
class Solution:
    def missing_number(self, arr: List[int]) -> int:
        # arr[-1] = arr[0] + (n-1)d 
        # Sum of AP = (2*arr[0] + d(n-1)) * n//2
        # Sum of AP = (arr[0] + arr[-1]) * n//2
        # Removed number = sum of AP - sum of arr
        n = len(arr)+1
        return (arr[0] + arr[-1]) * n//2 - sum(arr)

# Time: O(n) as time complexity of sum() function is O(n) in python
# Space: O(1)

