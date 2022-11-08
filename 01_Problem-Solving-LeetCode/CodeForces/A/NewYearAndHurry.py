__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/750/A

Solution: Brute-force approach. Initialize the total time taken by k since that is anyways needed for the commute to 
the party. Now see if its safe to solve the ith problem and still not exceed the minutes to midnight, if so proceed
with the iteration. If not, return the previous i as the answer. If all the problems can be solved, return n.
TODO: This should be solvable optimally via binary search as well. 
'''


def solve(n, k):

    min_to_midnight = 240
    total = k

    for i in xrange(1, n+1):
        this_prob = 5 * i
        if total + this_prob <= min_to_midnight:
            total += this_prob
        else:
            return i-1

    return n


if __name__ == "__main__":

    n, k = map(int, raw_input().split(" "))
    print solve(n, k)
