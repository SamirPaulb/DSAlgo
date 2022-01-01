# https://www.youtube.com/watch?v=x5hQvnUcjiM&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=23
# https://www.geeksforgeeks.org/printing-longest-common-subsequence/

X = "AGGTAB"
Y = "GXTXAYB"
m = len(X); n = len(Y)

dp = [[0]*(n+1) for i in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if X[i-1] == Y[j-1]:
            dp[i][j] = 1 + dp[i-1][j]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# for printing longest common subsequence
i = m; j = n
res = ""
while i > 0 and j > 0:   # if any of this i and j becomes 0 means one string is empty 
    if X[i-1] == Y[j-1]: # if character matches 
        res += X[i-1]    # add that to result string
        i -= 1; j -= 1   # move diagonally up
    else:                # else find the max of up and right position of dp table and move accordingly to up or left
        if dp[i][j-1] > dp[i-1][j]: 
            j -= 1
        else:
            i -= 1

print(res[::-1])         # reverse the string as we started from last

