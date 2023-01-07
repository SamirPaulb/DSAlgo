# https://leetcode.com/problems/count-numbers-with-unique-digits/

'''
n = 2
From 11 -> 20 => 11,22,33,..99 excluded. 
so ans = 10(for 1->10) + 9*9(as 1 element excluded in each 10 range). = 10 + 81 = 91

n = 3
for 1 -> 100 => ans = 91
From 101 -> 200 => (100,101), (110,112,113...119), (121,122),..(191,199) excluded.
ans(100, 199) = 8*9
From 201 -> 300 => (200,202), (211,212), (220,221,222...229),..(292,299) excluded.
ans(200, 299) = 8*9
.
.
ans(100, 1000) = 8*9*9
Total ans = 10 + 8*9*9 = 739

So Pattern = ans + 9*(11-i) ans i = [2,n]
'''

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0: return 1
        if n == 1: return 10
        
        ans = 10
        tmp = 9
        for i in range(2, n+1):
            tmp *= (11 - i)
            ans += tmp
            
        return ans
    

# Dynamic Programming

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        dp = [1, 10]
        for i in range(2, n+1):
            tmp = 81
            for j in range(1, i-1):
                tmp *= (9 - j)
            ans = dp[i-1] + tmp
            dp.append(ans)
        
        return dp[n]
                
