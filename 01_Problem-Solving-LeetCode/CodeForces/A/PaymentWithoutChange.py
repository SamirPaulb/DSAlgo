__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1256/A

Solution: At the first look it does appear as a coin change DP problem but we don't need to use that since we have to 
only check if the payment is possible and only two types of bills are available. 
First, we observe that no matter how many $n bills we have, we cannot do the payment if we don't have the S%n number of
$1 bills. Therefore we check that first.
Second, we can now be assured we have no issues of divisibility and hence we just need money >= to the required $S. Hence
we compute that sum of a * $n and b * $1 is >= $S. Return the decision string accordingly. 

Tidbit: 
Ternary operator:
Python: [on_true] if [expression] else [on_false] 
Java: [expression] ? [on_true] : [on_false] 
'''


def solve(a, b, n, S):

    # check the presence of enough $1 bills
    if S % n > b:
        return "NO"

    # check the total money value is enough to build $S
    return "YES" if (a * n) + (b * 1) >= S else "NO"


if __name__ == "__main__":
    testcases = int(raw_input())
    results = list()
    for testcase in xrange(0, testcases):
        a, b, n, S = map(int, raw_input().split(" "))
        results.append(solve(a, b, n, S))
    for result in results:
        print result
