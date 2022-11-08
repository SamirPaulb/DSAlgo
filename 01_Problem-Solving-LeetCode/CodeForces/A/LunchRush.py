__author__ = 'Devesh Bajpai'

import sys

'''
http://codeforces.com/problemset/problem/276/A
Algorithm: Just use the condition given in question (whether for current hotel, the t_i is more than k or not.
Catch here is to set the initial value of maximum which will be minimum possible value for integer and not 0.
'''

def solve(k,vals):


    maximum = -sys.maxint-1
    curr = -1
    for i in range(0,len(vals)):
        if(vals[i][1]>k):
            curr = vals[i][0] - (vals[i][1]-k)
        else:
            curr = vals[i][0]

        maximum = max(curr,maximum)

    return maximum


if __name__ == "__main__":
    n,k = map(int,raw_input().split(" "))
    vals = list()
    _n = 0
    while(_n < n):
        f,t = map(int,raw_input().split(" "))
        vals.append([f,t])
        _n+=1

    print solve(k,vals)