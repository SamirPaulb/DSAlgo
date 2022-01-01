# https://www.youtube.com/watch?v=SZqAQLjDsag&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=14
# https://practice.geeksforgeeks.org/problems/rod-cutting0840/1

class Solution:
    def cutRod(self, price, n):
        # as weight of Ub=nbounded Knapsack is length in rod cutting problem
        # so making a lenght arr with all possible length in which we can cut the rod
        length = [(i+1) for i in range(n)]
        
        dp = [[0]*(n+1) for i in range(n+1)]
        
        # in 1st row size of the rod is zero; so not cut possible so profit zero
        # in 1st column price array = 0; so for any cut no prfite
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if length[i-1] <= j:
                    dp[i][j] = max(price[i-1] + dp[i][j-length[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
        