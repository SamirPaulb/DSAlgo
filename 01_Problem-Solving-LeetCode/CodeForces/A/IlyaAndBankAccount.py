__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/313/A

Solution: If the number is positive, it is returned as is. Else we need to build the two possibilities. Since the
modulo operator works differently with -ve numbers, I convert the number into positive and then convert those 
possibilities into -ve for their final value. Return the max of them. 
'''


def solve(n):

    if n >= 0:
        return n

    n *= -1 # for ease of calculation
    num_without_last_digit = -(n / 10)
    num_without_second_last_digit = -(n / 100 * 10 + n % 10)
    return max(num_without_last_digit, num_without_second_last_digit)


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)
