# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sep = sorted(zip(startTime, endTime, profit), key = lambda x:x[1])
        endDP = [0]
        profitDP = [0]
        for s,e,p in sep:
            # right most element whose endTime <= current start time. 
            i = self.bisect_right(endDP, s) - 1 
            curProfit = profitDP[i] + p
            if curProfit > profitDP[-1]:
                profitDP.append(curProfit)
                endDP.append(e)
        
        return profitDP[-1]
    
    def bisect_right(self, arr, target): 
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return l
    
    
    
# Time: O(N * log(N))
# Space: O(N)
