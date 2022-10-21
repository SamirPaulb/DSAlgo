class Solution:
    def shipWithinDays(self, wt: List[int], days: int) -> int:
        l = max(wt); r = sum(wt); res = l
        
        def isValid(mid, days):
            r = 1
            s = 0
            for i in wt:
                s += i
                if s > mid:
                    r += 1
                    s = i
            return r <= days
        
        while l <= r:
            mid = (l + r) // 2
            if isValid(mid, days):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        
        return res