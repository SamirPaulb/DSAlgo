__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1326/B

Solution: Let's solve this mathematically.

x_0 = 0

b_0 = a_0 - x_0
=> b_0 + x_0 = a_0
=> b_0 = a_0 

b_1 = a_1 - x_1
=> b_1 + x_1 = a_1
=> b_1 + max(0,a_0) = a_1

b_2 = a_2 - x_2
=> b_2 + x_2 = a_2
=> b_2 + max(0,a_0,a_1) = a_2


Hence extrapolating it further, for ith term in the series, we have

b_i + max(0,a_0,a_1,....a_(i-1)) = a_i 

Hence the current value of x would be maximum of all the values of a from 0 to i-1. That can be kept as a running 
variable. Once a_i is calculated, the current value of x can be updated by checking its value against a_i and picking
the maximum. 

Return the string version of the list (separated by spaces)

'''


def solve(n, b):

    a = [None] * n
    a[0] = b[0]
    curr_x = max(0, a[0])

    for i in xrange(1,n):

        a_i = b[i] + curr_x
        a[i] = a_i
        curr_x = max(curr_x,a_i)

    return ' '.join(str(a_i) for a_i in a) #join requires an iterable, hence need to loop and convert each element as string


if __name__ == "__main__":
    n = int(raw_input())
    b = map(int, raw_input().split(" "))
    print solve(n, b)
