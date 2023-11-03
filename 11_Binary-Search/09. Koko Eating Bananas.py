# https://leetcode.com/problems/koko-eating-bananas/
# https://github.com/SamirPaulb/DSAlgo/blob/main/11_Binary-Search/01.%20Allocate%20Minimum%20Number%20Of%20Pages.py

class Solution:
    def minEatingSpeed(self, piles, h):
        def isValid(speed):
            time = 0
            for num in piles:
                time += math.ceil(num/speed)
            return time <= h
        
        l, r, res = 1, max(piles), max(piles)
        while l <= r:
            mid = l + (r-l)//2
            if isValid(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
    
    
# Time: O(N * log(M))      where M = max(piles)
# Space: O(1)
