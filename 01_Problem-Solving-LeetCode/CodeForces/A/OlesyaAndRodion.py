__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/584/A

Solution: The strategy that I follow is to make the 10s multiple of t which has n digits. Generating a 10s multiple
of t is easy, use t and then put zeroes. But since we need to have a bound of the number of digits in it, we 
first calculate the no. of digits in t. That much digits should be removed from n since those would be covered by
use t itself. In order to handle the case where we cannot generate the solution, we return -1. That is when the
no. of digits of t is greater than n.
'''


def solve(n, t):

    digits_t = count_digits(t)

    if n < digits_t:
        return -1

    n -= digits_t

    result = list()
    result.append(t)

    for _ in xrange(0, n):
        result.append(0)

    return "".join(str(_) for _ in result)


def count_digits(k):

    count = 0
    while k > 0:
        count += 1
        k /= 10
    return count


if __name__ == "__main__":

    n, t = map(int, raw_input().split(" "))
    print solve(n, t)
