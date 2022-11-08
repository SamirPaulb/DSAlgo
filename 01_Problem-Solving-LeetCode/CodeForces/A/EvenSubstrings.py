__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1139/A

Solution: For a string s, if we want to get the count of all the substrings ending with character at index k,
we'd have k+1 such substrings. To understand that, let's see an example:

String s = abcde has e as the character at the kth index, 
Hence the substrings are:
abcde
bcde
cde
de
e

Now in the light of this question, we just need to add this count every time we find a number divisible by
2 denoting the substrings ending at it would be even valued. 

~ Tidbit ~
ord() function provides the ASCII value of the passed character. Hence ord(c) - ord('0') would give
the actual integer value of the character c.  
'''


def solve(n, s):

    ord_zero = ord('0')
    even_nos = 0
    for i in xrange(0, n):
        if (ord(s[i])-ord_zero) % 2 == 0:
            even_nos += (i+1)

    return even_nos


if __name__ == "__main__":

    n = int(raw_input())
    s = list(raw_input())
    print solve(n, s)
