__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1206/A

Solution: Trick question. Since the numbers are all positive in both lists, if we pick the largest in each of the lists,
their sum is bound to be not in any of the lists. Find the maximums and return them. 
'''


def solve(n,a,m,b):

    return max(a), max(b)

if __name__ == "__main__":
    n = int(raw_input())
    a = map(int, raw_input().split(" "))
    m = int(raw_input())
    b = map(int, raw_input().split(" "))
    max_a,max_b = solve(n,a,m,b)
    print str(max_a) + " " + str(max_b)