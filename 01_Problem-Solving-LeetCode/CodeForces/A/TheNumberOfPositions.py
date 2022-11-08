__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/124/A
Solution: a is the lower limit of people in front, hence available spots are n-a. On the other hand, b is the upper
limit of people in back, hence available spots are n-(b-1). The minimum of both are the confirmed spots available.
'''


def solve(n,a,b):
    availableFront = n-a
    availableBack = n-b

    return min(availableFront,availableBack)



if __name__ == "__main__":

    n,a,b = map(int,raw_input().split(" "))

    print solve(n,a,b)