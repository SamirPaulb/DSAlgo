class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = max(days) + 1
        dp = [-1 for x in range(n)]
        #dp = [-1]*(max(days)+1)
        dp[0] = 0
        
        for x in range(1,len(dp)):
            if x in days:
                if x>=30:
                    #print(x,min(dp[x-1]+costs[0],dp[x-7]+costs[1],dp[x-30]+costs[2]))
                    dp[x] = min(dp[x-1]+costs[0],dp[x-7]+costs[1],dp[x-30]+costs[2])
                    
                elif x>=7 and x<30:
                    dp[x] = min(dp[x-1]+costs[0],dp[x-7]+costs[1],costs[2])
                    
                else:
                    dp[x] = min(dp[x-1]+costs[0],costs[1],costs[2])
                    
            else:
                dp[x] = dp[x-1]
                
        return dp[max(days)]
        