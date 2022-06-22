# https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1#

class Solution:
    def eggDrop(self,n, k):
        E = n  # number of eggs
        F = k  # number of floors
        memo = {}
        
        def solve(E, F):
            if E == 1: return F
            if F == 0 or F == 1: return F
            if (E,F) in memo: return memo[(E,F)]
            
            ans = 2**31
            for f in range(1, F):
                tmp = 1 + max(solve(E-1, f-1), solve(E, F-f))
                ans = min(ans, tmp)
            memo[(E,F)] = ans
            return memo[(E,F)]
        
        return solve(E, F)
        





# https://www.youtube.com/watch?v=gr2NtY-2QUY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=44
# https://leetcode.com/problems/super-egg-drop
'''
Base Cases:
i) If number of floor is 0 then we will attempt 0 times
ii) If number of floor is 1 then we will attempt 1 times
iii) If we have only 1 egg then we will try from floor 1 to floor n , So , here we done n attempts
Due to worst case we will try every floor and drop the egg
'''

import sys
class Solution:
    def superEggDrop(self, e, f): # e = total eggs; f = total floors
        dp = [[-1]*(10**4 + 1) for i in range(100 + 1)]
        def solve(e, f):
            if f == 0 or f == 1:  # if no. of floor 0 , 1 return n:
                return f
            if e == 1: return f   # if 1 egg return number of floor  
            if dp[e][f] != -1:    # previously we calculated solve(e, f) that is stored in dp[e][f]
                return dp[e][f]   # don't need to calculate again just return that value from here
            ans = sys.maxsize     # INT_MAX
            for k in range(1, f + 1):  # try from 1 to n floor , drop every floor and find minimum
                '''
                Here we have k eggs and n floor if we drop from i  (i=1 to n):
                i) egg break , now we remain k-1 eggs and i-1 floor beacase after i floor all the eggs will break
                ii) egg not break , now we remain k eggs and n-i floor because before i (included) all eggs will be remain
                '''
                temp = 1 + max(solve(e-1, k-1), solve(e, f-k)) # maximum at each floor k for worst case
                ans = min(ans, temp)  # Minimum attempts required from 1 to f
            dp[e][f] = ans  # storing recently calculated solve(e, f) in dp matrix for future use
            return ans
        
        return solve(e, f)
    

'''
Time Complexity: O((n^2) * k)
Space Complexity: O(k * n)
'''
# this Memoization-Recursive solution: TLE on LeetCode but Accepted on GeeksforGeeks!
   