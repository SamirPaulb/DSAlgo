__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1345/A

Solution: It requires drawing out couple of test cases which have n or m more than 2. Then
we observe a pattern, as soon as we have more adjoining surfaces, we don't have enough blanks
to accommodate the neighbors tabs. The pattern starts to develop when n = 2, m = 3 or other
way around. It has 7 shared surfaces but only 6 blanks. On this basis, we develop the if
condition and return the answer.  
'''


def solve(n, m):

    if n == 1 or m == 1 or n == m == 2:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n, m = map(int, raw_input().split(" "))
        results.append(solve(n, m))

    for result in results:
        print result
