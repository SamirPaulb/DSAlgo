__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1047/A

Solution: If n is divisible by 3, we can split it into 1,1 and n-2. Else, if the remainder would be 1 or 2
when n divided by 3, we can split it into 1, 2 and n-3. 
'''


def solve(n):

    if n % 3 == 0:
        return "1 1 " + str(n-2)
    else:
        return "1 2 " + str(n-3)


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)
