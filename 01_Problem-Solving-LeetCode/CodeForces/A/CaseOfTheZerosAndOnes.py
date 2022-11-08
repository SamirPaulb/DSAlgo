__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/556/A

Solution: Count the number of 1s and 0s. The absolute difference is the number of digits that would remain. 
Reason for this is, since we are removing 1 and 0 together, only the unpaired 1s or 0s will remain. 

Interesting problem. Good for interviews. 
'''

def solve(n, num):
    zeroCount = oneCount = 0

    for i in xrange(0, n):
        if num[i] == '0':
            zeroCount += 1
        else:
            oneCount += 1

    return abs(zeroCount - oneCount)


if __name__ == "__main__":
    n = int(raw_input())
    num = raw_input()
    print solve(n, num)