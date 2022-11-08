
__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/734/B

Solution: Since the objective is to maximize the sum, we prefer forming 256s over 32s. The minimum of k2, k5 and k6 tells
how many 256s are constructable. Once that is accomplished, we reduce k2 by it since we now try to build 32s.
Again, the minimum of k3 and remaining k2 tells how many 32s are constructable. These counts multiplied with their
respective numbers gives the total sum. 
'''


def solve(k2, k3, k5, k6):

    count_256 = min(k2, k5, k6)
    k2 -= count_256

    count_32 = 0
    if k2 > 0:
        count_32 = min(k2, k3)

    return (count_32 * 32) + (count_256 * 256)


if __name__ == "__main__":

    k2, k3, k5, k6 = map(int, raw_input().split(" "))
    print solve(k2, k3, k5, k6 )
