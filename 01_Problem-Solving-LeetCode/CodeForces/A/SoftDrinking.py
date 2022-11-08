__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/151/A

Solution: We first count the total drinks possible to be made, and the salt packs. With that we 
can get the total toasts possible. Since we do the toasts in batches of all people, we divide that
with n to get the total rounds of toast or no. of toast each person can have. 
'''


def solve(n, k, l, c, d, p, nl, np):

    drinks_count = min((k*l)/nl, c * d)
    salts_count = p / np
    toasts_count = min(drinks_count, salts_count)

    return toasts_count / n


if __name__ == "__main__":

    n, k, l, c, d, p, nl, np = map(int, raw_input().split(" "))
    print solve(n, k, l, c, d, p, nl, np)
