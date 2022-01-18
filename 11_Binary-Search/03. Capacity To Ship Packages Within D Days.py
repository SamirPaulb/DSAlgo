# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # First Solve => Allocate Minimum Number Of Pages - Binary Search
        
        l = max(weights);  r = sum(weights);  ans = -1
        
        if len(weights) < days: return -1
        
        def isValid(weight, days, mid):
            currSumWt = 0
            countOfDays = 1
            for wt in weights:
                currSumWt += wt
                if currSumWt > mid:
                    countOfDays += 1
                    currSumWt = wt
            if countOfDays > days: return False
            else: return True
        
        while l <= r:
            mid = (l+r) // 2
            if isValid(weights, days, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans