__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/219/A
Solution: Create a character frequency of the input character string. Iterate over it and
check, if the current character frequency is not a multiple of k, return -1. Otherwise,
append freq/k times of this character in result k-string. After the iteration,
return string made of k-Strings.
'''

from collections import Counter

def solve(str,k):
    mp = Counter(str)
    #print mp
    kstring = ""
    for key,val in mp.iteritems():
        if(val%k!=0):
            return -1
        else:
            #print val
            kstring += key*(val/k)

    #print result
    result = ""
    for i in range(0,k):
        result += kstring

    return result


if __name__ == "__main__":
    k = int(raw_input())
    str = raw_input()

    print solve(str,k)