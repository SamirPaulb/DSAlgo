__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1389/A

Solution: LCM(a,b) is the lowest multiple of the a and b. To fit a and b in a prescribed range,
a simple greedy strategy can be to take the smallest multiple of the smaller number which is
greater than itself. Say a < b. a * 1 returns a, hence the smallest multiple of a which is not
equal to a would be a * 2. If we cannot accommodate this in the range, the solution is impossible
and we default to -1.  
'''


def solve(l, r):

    if l * 2 <= r:
        result = [l, l * 2]
    else:
        result = [-1, -1]

    return str(result[0]) + " " + str(result[1])


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        l, r = map(int, raw_input().split(" "))
        results.append(solve(l, r))

    for result in results:
        print result
