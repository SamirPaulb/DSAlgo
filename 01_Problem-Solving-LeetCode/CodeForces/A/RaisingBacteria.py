__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/579/A

Solution: The solution requires counting the set bits in the given number n. This is because a power of 2 will always
be possible from 1 initial bacterium and that is the count of set bits a power of 2 has. All the other numbers need 
more set bits and those need to be counted. 
'''


def solve(n):

    count = 0
    while n > 0:

        count += (n & 1)
        n >>= 1

    return count


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)
