__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/688/B

Solution: If we observe the first few palindromes of even length, for the first 9 palindromes,
we get 11 to 99. After that, we go to 1001 and then put these 11 to 99 between two 1s. This results in
palindromes 1111, 1221, 1331 to 1991. If we observe the behavior, we see that this progression is like
the natural numbers. So the 5th such palindrome is 55, 9th is 99, 10th is 1001, 15th is 1551. Hence the
palindrome can be obtained by suffixing n with its reverse. 

Since we want to reverse n, it makes sense to keep the input in string itself. 
'''


def solve(n):

    return n + ''.join(reversed(n))


if __name__ == "__main__":

    n = raw_input()
    print solve(n)
