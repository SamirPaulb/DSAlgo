__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/474/B

Solution: First, we create a monotonically increasing array of prefix sums of worms count. This makes searching in 
it easy as we can exploit its sorted nature via binary search. We find the appropriate index for each given query
in it and update the result. We set end as mid when query <= worms_count[mid]. This way end would always point to
the appropriate pile after the binary search stops. 
'''


def solve(n, worms_count, m, queries):

    for i in xrange(1, n):
        worms_count[i] += worms_count[i-1]

    result = list()

    for _m in xrange(0, m):

        query = queries[_m]
        start = 0
        end = n

        while start < end:

            mid = start + (end - start)/2
            if worms_count[mid] < query:
                start = mid+1
            else:
                end = mid

        result.append(end+1) # question requires answer in 1 indexed notation

    for r in result:
        print r


if __name__ == "__main__":

    n = int(raw_input())
    worms_count = map(int, raw_input().split(" "))
    m = int(raw_input())
    queries = map(int, raw_input().split(" "))
    solve(n, worms_count, m, queries)
