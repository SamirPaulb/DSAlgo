# https://www.youtube.com/watch?v=823Grn4_dCQ&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=25

X = "AGGTAB"
Y = "GXTXAYB"
m = len(X); n = len(Y)

# Eleminate common subsequence elements

dp = [[0] * (n+1) for i in range(m+1)]
# in 0th row and 0th column No common subsecuence can be so 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if X[i-1] == Y[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

LCS = dp[-1][-1]  # LCS = 4  => "GTAB"
# After Eleminating common subsequence elements from X + Y; length of X + Y becomes = m + n - LCS
print(m + n - LCS)
