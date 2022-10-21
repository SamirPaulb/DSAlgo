import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        arr = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        arr.sort(key = lambda x:x[1])
        
        dpEndTime = [0]
        dpProfit = [0]
        for start, end, profit in arr:
            indx = bisect.bisect_right(dpEndTime, start)
            prevProfit = dpProfit[-1]
            curProfit = dpProfit[indx-1] + profit
            if curProfit > prevProfit:
                dpEndTime.append(end)
                dpProfit.append(curProfit)
        return dpProfit[-1]
