__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1369/B

Solution: Working through a few examples we can observe the any substring of type 10 can reduce to 0.
But what cannot be reduced is the 0s before that substring and the 1s after it. That is because the
former don't have at least one 1 before them and the later don't have at least one 0 after them. 
So first we check if that substring of 10 type exist. If not, the string is returned as is. If yes,
we need to find the leading 0s and the trailing 1s. That extra 0 in the middle is due to the substring
of type 10 reducing to 0. 

Also, lets workout a substring of pattern 10 and see how it can be reduced to 0:

say, s = 00 11101010001000100 11111
Using space to demarcate the leading 0s and trailing 1s.

Now lets reduce the middle substring:

11101010001000100
1101010001000100
111010001000100  
11010001000100
1010001000100
1010001000100
101000100010
10100100010
1010100010
10101010
1010100
101100
10100
1010
100
10
0 

Hence the s would become: 00 0 11111

There 2 leading 0s and 5 trailing 1s with the reduced 10 substring's 0 in the middle is the final answer.
 
'''


def solve(n, s):

    # check if there exists at least one occurrence of 10
    is_present_10 = False
    for i in xrange(1, n):

        if s[i-1] > s[i]:
            is_present_10 = True
            break

    if not is_present_10:
        return s

    # find the count of 0s till the first 1
    i = 0
    while i < n and s[i] == '0':
        i += 1

    leading_zeroes = i

    # find eh count of 1s till the first 0 from the back
    i = n-1
    while i >= 0 and s[i] == '1':
        i -= 1

    trailing_ones = n - i - 1

    return ('0' * leading_zeroes) + '0' + ('1' * trailing_ones)


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        s = raw_input()
        results.append(solve(n, s))

    for result in results:
        print result
