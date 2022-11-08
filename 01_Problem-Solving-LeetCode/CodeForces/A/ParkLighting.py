__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1358/A

Solution:
 CASE 1:
 If at least n or m is even, we can follow the strategy to half that dimension and put
lamps in the middle across the other dimension. e.g. n = 3, m = 2

 _ _
|_|_|
|_|_|
|_|_|

Here we put lamps across the vertical in n rows. So the total lamps used would be n * (m)/2 =
nm/2. Swapping n and m, we can solve when m is even and n is odd.

CASE 2:
Now for the case when both n and m are odd, we convert one of the dimension even and apply the above
strategy. Say we do it for n. Hene we use ((n-1) * m)/2 lamps. For the remaining section, we have
one row of m columns. For that we place a lamp between ever two cells, thereby using (m+1)/2 lamps.
So the total lamps used is ((n-1) * m)/2 + (m+1)/2 = (n * m + 1)/2.

Return the result accordingly. 


 
'''


def solve(n, m):

    if n % 2 == 0 or m % 2 == 0:
        return (n * m)/2
    else:
        return ((n * m) + 1)/2


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n, m = map(int, raw_input().split(" "))
        results.append(solve(n, m))

    for result in results:
        print result
