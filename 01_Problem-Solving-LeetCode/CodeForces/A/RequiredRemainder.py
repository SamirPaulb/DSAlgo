__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1374/A

Solution: Since is the upper limit of the range, we get the quotient and remainder by dividing it by x. Now if the 
required remainder (i.e. y) is less than or equal to the one got, we can safely multiply quotient by x and add y to it
to get the largest possible k. Else, we need to try the last multiple of x, i.e quotient needs to be reduced by 1 and
then the result is calculated. 
'''


def solve(x, y, n):

    quotient = n / x
    remainder = n % x

    if y > remainder:
        quotient -= 1

    return (quotient * x) + y


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        x, y, n = map(int, raw_input().split(" "))
        results.append(solve(x, y, n))

    for result in results:
        print result
