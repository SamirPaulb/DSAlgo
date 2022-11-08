__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1352/A

Solution: The idea is do the digit extraction and multiply it with its current 10th power. Also make
sure that 0 is not added. 
'''


def solve(n):

    round_nums = list()
    power = 1

    while n > 0:

        digit = n % 10
        if digit != 0:
            round_number = digit * power
            round_nums.append(round_number)
        power *= 10
        n /= 10

    return str(len(round_nums)) + "\n" + " ".join(str(_) for _ in round_nums)


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        results.append(solve(n))

    for result in results:
        print result
