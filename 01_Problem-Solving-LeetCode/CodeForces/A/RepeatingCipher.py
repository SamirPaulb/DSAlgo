__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1095/A

Solution: Straightforward. Keep a counter for step that increments on every iteration round and that is the update
given to the iterator of the string. Use this iterator to extract the first character of each group of the cipher
and add that to the result. 
'''


def solve(n, s):

    result = list()
    i = step = 0

    while i < n:
        result.append(s[i])
        step += 1
        i += step

    return "".join(result)


if __name__ == "__main__":

    n = int(raw_input())
    s = raw_input()
    print solve(n, s)
