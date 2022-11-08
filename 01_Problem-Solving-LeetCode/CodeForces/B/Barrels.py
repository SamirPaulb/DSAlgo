__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1430/B

Solution: Since we want to pour from the most filled barrels so that difference is higher, we firstly
sort the barrels in decreasing order. Then we add together the first k elements to get the joint content
of poured in barrels. Since the barrel from which the liquid has been poured out would turn 0, the max
difference would be this joint bigger barrel - 0. Hence we just need find that sum of first k elements.
Care should be taken if we don't go beyond n since we could have k > n. 
'''


def solve(n, k, barrels):

    barrels.sort(reverse=True)

    biggest_barrel = barrels[0]
    rounds = 0
    i = 1
    while rounds < k and i < n:
        biggest_barrel += barrels[i]
        i += 1
        rounds += 1

    return biggest_barrel


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n, k = map(int, raw_input().split(" "))
        barrels = map(int, raw_input().split(" "))
        print solve(n, k, barrels)
