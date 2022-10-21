class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        am = (int(arriveAlice[:2]), int(leaveAlice[:2]))
        ad = (int(arriveAlice[3:]), int(leaveAlice[3:]))
        
        bm = (int(arriveBob[:2]), int(leaveBob[:2]))
        bd = (int(arriveBob[3:]), int(leaveBob[3:]))
        
        # print(am, ad, bm, bd)
        
        start_month = max(am[0], bm[0])
        end_month = min(am[1], bm[1])
        # print(start_month, end_month)
        if start_month == end_month:
            if am[0] == bm[0] == start_month:
                ans = min(ad[1], bd[1]) - max(ad[0], bd[0]) + 1
            elif am[0] == start_month:
                ans = min(ad[1], bd[1]) - ad[0] + 1
            elif bm[0] == start_month:
                ans = min(ad[1], bd[1]) - bd[0] + 1 
            else:
                ans = min(ad[1], bd[1]) - max(ad[0], bd[0]) + 1
            # print(ad[1], bd[1], ad[0], bd[0])
            return ans if ans > 0 else 0
        
        res = 0
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for month in range(start_month, end_month+1):
            if month == start_month:
                if start_month == am[0] == bm[0]: res += days[month-1] - max(ad[0], bd[0]) + 1
                elif start_month == am[0]: res += days[month-1] - ad[0] + 1
                else: res += days[month-1] - bd[0] + 1
            elif month == end_month:
                if end_month == am[1] == bm[1]: res += min(ad[1], bd[1])
                elif end_month == am[1]: res += ad[1]
                else: res += bd[1]
            else:
                res += days[month - 1]
        
        return res