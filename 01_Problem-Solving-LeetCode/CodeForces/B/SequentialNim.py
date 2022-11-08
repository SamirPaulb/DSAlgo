__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1382/B

Solution: Till the players land on a pile having more than 1 stone in it, there isn't any strategy to employ. Each 
player picks the 1 stone in the pile. Once this ends, the player to play can strategically pick s-1 stones in the current
pile (having s stones), thereby forcing the next player to pick the one stone left. This makes the first player to be
in command again. If the player lands on the last pile, the strategy is to collect all the stones thereby
depriving the other player to play and losing. Hence we need to find the prefix of 1-stone piles in the given piles. 
If that count is even, the second player wins, otherwise the first player wins.
The exception to this strategy is the case where there are all 1s. As mentioned above, there isn't any strategy to 
employ and the number of the piles (n) determine who wins. If its odd, second player wins, otherwise the first player
wins.   
'''


def solve(n, arr):

    i = 0
    while i < n and arr[i] == 1:
        i += 1

    if i == n:
        if n % 2 == 0:
            return "Second"
        else:
            return "First"
    else:
        if i % 2 != 0:
            return "Second"
        else:
            return "First"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        results.append(solve(n, arr))

    for result in results:
        print result
