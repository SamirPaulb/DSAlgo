__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/509/A

Solution: The brute-force nxn grid solution seems quite obvious. Let's make some space optimization to that solution.  

Say n = 5. So the first row and the first cell of next row looks like this.

1 1 1 1 1
1

Now if you observe, the next cell to be calculated here is for 2nd row and 2nd column. Its value only depends on the
previous row and previous column neihbors. Hence we don't need to preserve the whole grid. We we are process row-wise,
we just need to preserve the previous row which itself will be updated for the current row. Also, we need to keep 
track of the previous column, which can be done via a variable. This brings the space complexity from n^2 to n. 

'''


def solve(n):

    row = [1] * n #nice way to create a list repeated with the same value for the given times

    for i in xrange(1, n):

        prevCol = 1

        for j in xrange(1, n):

            row[j] = row[j] + prevCol
            prevCol = row[j]

    print row[n-1]


if __name__ == "__main__":

    n = int(raw_input())
    solve(n)