__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1316/A

Solution: Since the average has to be same before and after the change, the sum of grades should be same. That means
we can set all the other students at 0 and set a1 student as the sum of the grades. But we cannot have the score
greater than m. Hence it has to be min(sum, m).  
'''


def solve(m, arr):

    return min(sum(arr), m)


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        __, m = map(int, raw_input().split(" ")) # ignoring n since we don't use it
        arr = map(int, raw_input().split(" "))
        print solve(m, arr)
