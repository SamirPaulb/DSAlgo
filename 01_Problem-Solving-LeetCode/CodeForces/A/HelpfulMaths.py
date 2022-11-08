__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/339/A

Solution: Split the expression by +. Sort the resulting list and return the list joined by +. Also take care of inputs
with +, which should be returned as is. 
'''


def solve(s):

    if "+" not in s:
        return s

    nums = map(int, s.split("+"))
    nums.sort()
    return "+".join(str(num) for num in nums)


if __name__ == "__main__":

    s = raw_input()
    print solve(s)
