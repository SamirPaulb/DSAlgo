__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/988/A

Solution: Using a brute-force approach, where a visited boolean array checks the presence of a number being seen or not.
This insures distinctness constraint. A result list maintains the final indices but indexed at 1. 
As soon as the result list since reaches k, we return the decision YES and result list. If the loop that traverses on the
numbers exhausts and the result list hasn't reached k, the decision NO and null is returned. 
'''


def solve(n, k, nums):
    visited = [False for _ in range(101)]
    result = []
    currResultSize = 0

    for i in xrange(0, n):

        num = nums[i]
        if not visited[num]:

            visited[num] = True
            result.append(i+1) #since the index referred in this problem starts at 1 instead of 0
            currResultSize += 1

            if currResultSize == k:
                return "YES", result

    return "NO", None


if __name__ == "__main__":
    n, k = map(int,raw_input().split(" "))
    nums = map(int,raw_input().split(" "))
    decision, results = solve(n, k, nums)

    print decision
    if decision == "YES":
        print ' '.join([str(result) for result in results])
