__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1355/A

Solution: The extraction of digits is usual and that helps to calculate the product of maximum and minimum digits
in the number in each iteration of k. The improvement is that we don't need to calculate all the values since
it could happen that the minimum digit becomes 0, which causes the product between the maximum and minimum digits
0 and hence all the subsequent numbers in the series are same as their previous one. So we stop the iteration early
and return the value of a at that point.  
'''


def solve(a, k):

    while k > 1:

        prod = prod_min_max_digits(a)
        a += prod
        if prod == 0:
            break
        else:
            k -= 1

    return a


def prod_min_max_digits(a):

    min_digit = a
    max_digit = -1

    while a > 0:
        d = a % 10
        min_digit = min(min_digit, d)
        max_digit = max(max_digit, d)
        a /= 10

    return min_digit * max_digit


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        a, k = map(int, raw_input().split(" "))
        results.append(solve(a, k))

    for result in results:
        print result
