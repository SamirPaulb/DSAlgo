# https://youtu.be/cETfFsSTGJI
# Find The indeces Path of jump from 0th index to reach last index so that number of jumps are minimum
nums = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]

n = len(nums)
dp = [0]*n
jumpIndex = [0]*n

for i in range(1, n):
    for j in range(i):
        if j + nums[j] >= i:          # check if we can directly reach i from j
            if dp[i] == 0:            # previously no one has reached i 
                dp[i] = dp[j] + 1     # update
                jumpIndex[i] = j      # keeping a track from which index we jumped to reach i 
            else:
                if dp[j] + 1 < dp[i]: # update only if current jumps is lesser
                    dp[i] = dp[j] + 1
                    jumpIndex[i] = j  # keeping a track from which index we jumped to reach i

res = []
j = n-1
while j > 0:         # traverse from n-1 to 0 to find the path of min jumps 
    res.append(j)
    j = jumpIndex[j]
res.append(0)        # as always we have to traverse from 0

res.reverse() 
print(res)           # indeces of path are = [0, 1, 4, 5, 9]

# Time: O(n^2)
# Space: O(n)