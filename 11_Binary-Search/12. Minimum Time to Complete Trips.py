# https://leetcode.com/problems/minimum-time-to-complete-trips/

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def check(curTime):
            tripsCount = 0
            for t in time:
                tripsCount += curTime // t
            return tripsCount >= totalTrips
        
        l = 0
        r  = min(time) * totalTrips + 1
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
    
    
    
# Time: O(N log(N))
