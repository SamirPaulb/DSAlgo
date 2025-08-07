# https://m.youtube.com/watch?v=8q0CZ748pz4

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        
        def solve(i, j):
            if i == j == 0:
                return 1
            if i < 0 or j < 0 or abs(i - j) > 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            ans = 0
            if i == j:
                ans += solve(i-1, j-1)     # vertical domino
                ans += solve(i-2, j-2)     # two horizontal dominos
                ans += solve(i-1, j-2)     # L tromino
                ans += solve(i-2, j-1)     # reverse L tromino
            elif i > j:
                ans += solve(i-2, j)       # vertical domino on left
                ans += solve(i-2, j-1)     # tromino
            else:  # j > i
                ans += solve(i, j-2)
                ans += solve(i-1, j-2)

            memo[(i, j)] = ans % MOD
            return memo[(i, j)]

        return solve(n, n)


# Time: O(N)    # as abs(i-j) <= 1 so both going from n->1 togother, so technically only 1 variable changing
# Space: O(N*N)




##########################################



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
