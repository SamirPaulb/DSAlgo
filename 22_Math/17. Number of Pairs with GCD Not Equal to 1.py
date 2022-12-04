''' 
Problem: You are given two arrays A and B. For every i in [1,n] find the number of pairs (i,j) such that
gcd(A[i], B[j]) != 1

n = number of elements in both arrays
1 <= n <= 10^5
1 <= Ai, Bi <= 10^6

Sample Testcase:
n = 2
A = 2 4
B = 4 2

Output: 4
// 1 - based indexing
Explanation: pairs (A[1], B[1]), (A[1], B[2]), (A[2], B[1]), (A[2], B[2]) have gcd != 1. So total 4 pairs

So basically we have to count number of pairs (contains one element from both arrays) whose gcd > 1
Been scratching my head for a long time but couldn't find a solution better than O(n^2).
Can any math genius help me in solving this
'''

import collections

A = [2, 3, 5, 6, 9, 30, 15]
B = [5, 8, 18, 7, 21, 14]


freqA = collections.Counter(A)
freqB = collections.Counter(B)
maxElem = max(max(A), max(B))

res = 0
dp = [0] * (maxElem + 1)

for i in range(maxElem, 1, -1):
    cntA = cntB = subtract = 0
    for j in range(i, maxElem+1, i):
        cntA += freqA[j]
        cntB += freqB[j]
        subtract += dp[j]
    pairsWithGcdMultipleOfi = cntA * cntB
    pairsWithGcdExactlyi = pairsWithGcdMultipleOfi - subtract
    dp[i] = pairsWithGcdExactlyi
    res += dp[i]

print(res)

