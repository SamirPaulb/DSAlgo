__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/519/B

Solution: Calculate the sum of each round of errors. The difference of first and second will give the error resolved
by second round. Similarly, the difference of second and third will give the error resolved by third round.   
'''


def solve(first_errors, second_errors, third_errors):

    first_sum = sum(first_errors)
    second_sum = sum(second_errors)
    third_sum = sum(third_errors)

    print first_sum - second_sum
    print second_sum - third_sum


if __name__ == "__main__":

    raw_input() # ignoring n
    first_errors = map(int, raw_input().split(" "))
    second_errors = map(int, raw_input().split(" "))
    third_errors = map(int, raw_input().split(" "))

    solve(first_errors, second_errors, third_errors)
