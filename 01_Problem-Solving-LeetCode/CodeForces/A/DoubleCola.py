'''
https://codeforces.com/problemset/problem/82/A

Solution: See the following example:

S, L, P, R, H  | total = 5
S,S, L,L, P,P, R,R, H,H  | total = 5 + 10 = 15
S,S,S,S, L,L,L,L, P,P,P,P R,R,R,R H,H,H,H  | total = 5 + 10 + 20 = 35
and so on.

Say n = 23.
The first idea is to estimate the row where the nth person would belong. For that, we iterate over the doubling
the rate and reducing the net people count left after processing each row, till we can.

Finally n will be smaller than the 5 * rate. Hence we now need to figure out the column in this row.
Since rate would be showing the total number of people of each kind, if we divide the remaining n with rate, we
should get the column.

Important, we do n-1 in estimating the column since array is indexed from 0, but n would count from 1.

Interesting problem. Good for interviews.
'''

def solve(n):

    map = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

    rate = 1

    #estimating the row
    while (5 * rate) <= n:
        n -= (5 * rate)
        rate *= 2

    #estimating the column in that row
    return map[(n-1)/rate]


if __name__ == "__main__":
    n = int(raw_input())
    print solve(n)