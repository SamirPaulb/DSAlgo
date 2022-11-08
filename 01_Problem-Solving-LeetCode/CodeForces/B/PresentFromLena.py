__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/118/B

Solution: First we need a logic to generate all rows. For a give number n, it has 2n rows. We can set the loop from -n
to n which makes it easy to still access values not doubled by using abs. For each row, a max_value is the highest number
that we reach to while incrementing, and then start decrementing. That is calculated n - row or n - abs(row) to handle
-ve row numbers.  
there are three parts:
1. Generate the spaces which is 0 to row-1
2. Generate the increment of numbers from 0 to max_value-1
3. Generate the decrement of numbers from max_value to 0
'''


def solve(n):

    space_deliminator = " "
    for row in xrange(-n, n+1):
        max_value = n - abs(row)
        this_line = ""
        # add the spaces
        for i in xrange(0, abs(row)):
            this_line += (2 * space_deliminator)
        # incremental loop
        for i in xrange(0, max_value):
            this_line += str(i) + space_deliminator
        # decremental loop
        for i in xrange(max_value, -1, -1):
            this_line += str(i) + space_deliminator
        # remove that one extra space after the last 0
        print this_line[:-1]


if __name__ == "__main__":
    n = int(raw_input())
    solve(n)
