# https://www.youtube.com/watch?v=ot_XBHyqpFc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=12
# Count of the number of subsets with a given Differnce => s1 - s2 = diff 
arr = [1, 1, 2, 3]
diff = 1

# s1 - s2 = diff        ---(1)
# s1 + s2 = sum(arr)    ---(2)

# (1) + (2) we get,
# 2 * s1 = diff + sum(arr)
# s1 = (diff + sum(arr)) // 2
# now this problem reduces to count of subset sum problem of Dynamic programming
target = (diff + sum(arr)) // 2

dp = [[0] * (target + 1) for i in range(len(arr) + 1)] 

# Changing 1st row of dp = 0; as with arr size 0 no subset sum is possible to be equal to j
for j in range(target + 1):
    dp[0][j] = 0

# Changing 1st column of dp = 0; as with target = 0, 1 empty subset is always possible
for i in range(len(arr) + 1):
    dp[i][0] = 1

# Change the remaining dp with target
for i in range(1, len(arr) + 1):
    for j in range(1, target + 1):
        if arr[i - 1] <= j:
            dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1]) # dp[len(arr)][target]


