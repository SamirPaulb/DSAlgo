__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1183/A

Solution: Using the brute-force method to generate all integers >= n, and checking if their digits' sum is divisible
by 4. The answer is bound to occur to using a while true doesn't hurt.
'''


def solve(n):

    candidate = n
    while True:

        if is_digit_sum_div_4(candidate):
            return candidate
        else:
            candidate += 1


def is_digit_sum_div_4(n):

    sum = 0
    while n > 0:
        sum += n % 10
        n /= 10

    return sum % 4 == 0


if __name__ == "__main__":
    n = int(raw_input())
    print solve(n)
