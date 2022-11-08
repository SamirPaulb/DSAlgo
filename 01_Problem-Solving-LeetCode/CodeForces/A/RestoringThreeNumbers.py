__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1154/A

Solution: Since the sums are all positive, that means at least one of them would be positive. That means, the largest 
of the 4 sums would the joint sum (a + b + c), which is found in the first iteration. In the second loop, we exclude 
that value, and subtract all the other sums from this joint sum to find the individual numbers (in any order). 
'''


def solve(x_arr):

    a_plus_b_plus_c = x_arr[0]
    for i in xrange(1, 4):

        if x_arr[i] > a_plus_b_plus_c:
            a_plus_b_plus_c = x_arr[i]

    nums = list()
    for i in xrange(0, 4):

        if x_arr[i] != a_plus_b_plus_c:
            nums.append(a_plus_b_plus_c - x_arr[i])

    return " ".join(str(elem) for elem in nums)


if __name__ == "__main__":

    x_arr = map(int, raw_input().split(" "))
    print solve(x_arr)

