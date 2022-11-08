__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/581/B

Solution: Since we need a house to be taller than its neighbors on the right, we iterate the list from right to left.
If the current height is <= largest seen so far, we ned make it luxurious by taking its diff with the later and adding
1 to it. If the height is > largest seen so far, its already luxurious and we need to update the largest seen so far
as this height. 
'''


def solve(n, h_arr):

    h_increment = [0] * n

    largest = h_arr[n-1]
    for i in xrange(n-2, -1, -1):

        if h_arr[i] <= largest:
            h_increment[i] = largest - h_arr[i] + 1
        else:
            largest = h_arr[i]

    return " ".join(str(h_inc) for h_inc in h_increment)


if __name__ == "__main__":

    n = int(raw_input())
    h_arr = map(int, raw_input().split(" "))
    print solve(n, h_arr)
