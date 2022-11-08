__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1220/A

Solution: We need to find distinct characters that can signify the presence of 0 and 1. Those are z and n respectively.
Hence we iterate over the string, for every 'z', we append 0 to the result and for every 'n', we prepend 1 to it.
Finally return the result joined by space. 
'''


def solve(n, jumbled):

    result = list()

    for i in xrange(0, n):
        if jumbled[i] == 'z':
            result.append('0') # append
        elif jumbled[i] == 'n':
            result.insert(0, '1') # prepend

    return " ".join(result)


if __name__ == "__main__":

    n = int(raw_input())
    jumbled = raw_input()
    print solve(n, jumbled)
