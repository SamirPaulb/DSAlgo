__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/61/A

Solution: Brute force, where we compare each corresponding characters of both numbers, thereby adding 0 when same and
1 when different to the resultant string. 
'''


def solve(num1, num2):

    n = len(num1)
    result = [''] * n

    for i in xrange(0, n):

        if num1[i] == num2[i]:
            result[i] = '0'
        else:
            result[i] = '1'

    return "".join(result)


if __name__ == "__main__":

    num1 = raw_input()
    num2 = raw_input()
    print solve(num1, num2)
