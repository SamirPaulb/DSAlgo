__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1295/A

Solution: We can observe a fact that the least number of segments (= 2) are needed to make a '1'. So if we could
use 4 segments, we can make '11' instead of '4'. But if the segments given are odd, we will be left with 1 unused
segment after making n/2 '1'. To handle this case, we make a '7' using 3 segments. Since '71' is greater than
'17', we can deduce an algorithm:

if n is odd, use 3 segments to start the number with one '7'.
Then put n/2 '1's. 
'''


def solve(n):

    big_num = list()

    if n % 2 != 0:
        big_num.append('7')
        n -= 3

    big_num += ['1'] * (n/2)

    return "".join(big_num)


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        results.append(solve(n))

    for result in results:
        print result
