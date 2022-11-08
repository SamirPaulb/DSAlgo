__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/749/A

Solution: Since we want maximum number of primes to represent n, we will use the smallest primes to build it. If n is
even, it would have n/2 2s. If its odd, we would replace the last 2 with a 3. Since we have to also give the number of
primes in the result (which is n/2), we append that to the result.
'''


def solve(n):

    result = [2] * (n/2)
    if n % 2 != 0:
        result[(n/2)-1] = 3

    return str(n/2) + "\n" + " ".join(str(elem) for elem in result)


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)
