__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/318/A
Algorithm: Find the half of the limit number.
Check if it lies on the left of the half of it. If so, print the kth odd number.
Check if it lies on the right of the half of it. If so, print the kth even number.
'''


def solve(n,k):
    if(n%2==0):
        half = n/2
    else:
        half = n/2 + 1

    if(k<=half):
        return (2*k)-1
    else:
        return 2*(k-half)

if __name__ == "__main__":
    n,k = map(int,raw_input().split(" "))
    print solve(n,k)
