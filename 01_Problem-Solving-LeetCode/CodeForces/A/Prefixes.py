__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1216/A

Solution: We iterate over the string in steps of 2 and check every pair of adjacent characters. If they are same, we 
make one of them (say the left one) different from its right neighbor. A counter counts the operations done and finally
that along with the modified string is returned as a result.  
'''


def solve(n, s):

    ops = 0
    for i in xrange(0, n, 2):

        if s[i] == s[i+1]:

            ops += 1
            if s[i] == 'a':
                s[i] = 'b'
            else:
                s[i] = 'a'

    return str(ops) + "\n" + "".join(s)


if __name__ == "__main__":

    n = int(raw_input())
    s = list(raw_input())
    print solve(n, s)
