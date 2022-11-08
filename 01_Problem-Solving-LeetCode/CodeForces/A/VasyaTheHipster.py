__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/581/A

Solution: The minimum of red and blue socks would give us the no. of days of different socks. As we run out of one of 
them, we will use the larger of those two for the remaining days. We would have used the different sock days worth of 
solo socks of that type, and dividing the remaining with 2 would give us the same sock days. 
'''


def solve(a, b):

    diff_sock_days = min(a, b)
    same_sock_days = (max(a, b) - diff_sock_days) / 2

    return str(diff_sock_days) + " " + str(same_sock_days)


if __name__ == "__main__":

    a, b = map(int, raw_input().split(" "))
    print solve(a, b)

