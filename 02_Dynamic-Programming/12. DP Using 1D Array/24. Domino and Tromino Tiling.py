# https://leetcode.com/problems/domino-and-tromino-tiling/
# https://youtu.be/7cijrfUkQzc

'''
Purely based on observation and by intuition you can arrive at the follwing formula->
f(n)=f(n-1)+f(n-2)+2*(f(n-3)+f(n-4)+......+f(n-n))      ------(1)

if we remove 1 width  and 2 length tile vertically theres 1 way
if we remove 1 horizontal 2 width and 1 length tile below will also be same width tile so only 1 way
if we remove 3,by obervation we get 2 ways    

similarly,
f(n-1) = f(n-2) + f(n-3) + 2*(f(n-4) + ....)   
f(n-2) = f(n-1) - f(n-3) - 2*(f(n-4) + f(n-5) + ....)   ------(2)
putting value of f(n-2) to equation (1) we get,

f(n) = 2*f(n-1) + f(n-3)

                         __     and         __
                                                                       |  __|          |__ |   
similarly 2 for rest 
'''


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0, 1, 2, 5] + [1] * n
        if n <= 3: return dp[n]
        
        for i in range(4, n+1):
            dp[i] = ((2 * dp[i-1]) % MOD + dp[i-3])% MOD
        
        return dp[n]
      
# Time: O(N)
# Space: O(N)
