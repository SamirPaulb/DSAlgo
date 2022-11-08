__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/456/A

Solution: We sort the list of laptops by price. Now we iterate over the laptops and check if the current laptop's price
is strictly smaller than that of its right neighbor, and its quality is strictly greater than its right neighbor, then
we've found the pair and break out of the loop. 
'''


def solve(laptops):

    # sort laptops by their price
    laptops.sort(key=lambda laptop: laptop[0])

    decision = "Poor"

    for i in xrange(0, len(laptops)-1):

        if laptops[i][0] < laptops[i+1][0] and laptops[i][1] > laptops[i+1][1]:
            decision = "Happy"
            break

    print decision + " Alex"


if __name__ == "__main__":

    n = int(raw_input())
    laptops = list()
    for _ in xrange(0, n):
        a, b = map(int, raw_input().split(" "))
        laptops.append([a, b])

    solve(laptops)
