__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/contest/1337/problem/B

Solution: The need is decide the ordering of spells. 
Void Absorption: VA : x/2 + 10
Lightening Strikes: LS: x - 10

if we do LS and then VA: (x-10)/2 + 10 = x/2 - 5 + 10 = x/2 + 5
if we do VA and then LS: x/2 + 10 - 10 = x/2

Hence we would want to do all the VAs till doing that actually reduces x. e.g. imagine x = 2.
Then x/2 + 10 = 11. Then in second round it becomes 11/2 + 10 = 15. So it stars growing. That is when
we need to employ LS. So once the VAs are over, we need to check we have enough LS to bring x to 0 or less.
This means x <= m * 10. Return the decision accordingly. 

'''


def solve(x, n, m):

    while x > 0 and n > 0 and x/2 + 10 < x:

        if n > 0:
            x = x/2 + 10
            n -= 1

    return "YES" if x <= m * 10 else "NO"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        x, n, m = map(int, raw_input().split(" "))
        results.append(solve(x, n, m))

    for result in results:
        print result
