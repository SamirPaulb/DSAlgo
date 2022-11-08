__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1108/A

Solution: Since a and b are inclusive the range limits, we can send those as answers. We are guaranteed that l1 != r1
and l2 != r2. All the other possible combinations can be equal, hence we check for 2 distinct values and return. 
'''


def solve(l1, r1, l2, r2):

    if l1 != l2:
        return l1, l2
    elif l1 != r2:
        return l1, r2
    elif l2 != r1:
        return l2, r1
    elif r1 != r2:
        return r1, r2


if __name__ == "__main__":
    test_cases = int(raw_input())
    results = list()
    for testcase in xrange(0, test_cases):
        l1, r1, l2, r2 = map(int, raw_input().split(" "))
        results.append(solve(l1, r1, l2, r2))
    for result in results:
        print str(result[0]) + " " + str(result[1])
