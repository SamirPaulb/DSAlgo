__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1228/A

Solution: The total number of unique digits in the numbers should be the total number of digits in it. Hence
the generate the numbers in the given range and validate against this constraint. 
'''


def solve(l, r):

    for candidate in xrange(l, r+1):

        if len(set(str(candidate))) == len(str(candidate)):
            return candidate

    return -1


if __name__ == "__main__":

    l, r = map(int, raw_input().split(" "))
    print solve(l, r)
