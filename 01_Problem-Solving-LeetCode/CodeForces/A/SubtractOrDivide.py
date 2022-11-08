__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1451/A

Solution: The only condition is not not use the number itself for its divisor. Hence if n is even, we divide it by
its half and then use that divisor to divide itself. That amounts to 2 moves. If n is odd, we first reduce it by 1 to 
make it even and then follow the above steps. That amounts to 2 + 1 = 3 moves. For n = 1,2 and 3, we handle it explicitly
since they are outliers to the above optimal methodology. 
'''


def solve(n):

    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n % 2 == 0:
        return 2
    else:
        return 3


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n = int(raw_input())
        print solve(n)
