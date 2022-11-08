__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/703/A

Solution: Nothing fancy. Just run the loop over the games and count the rounds won by Mishka and Chris. Return the result
accordingly. 
'''


def solve(games):

    mishka = chris = 0

    for game in games:

        if game[0] > game[1]:
            mishka += 1
        elif game[0] < game[1]:
            chris += 1

    return "Friendship is magic!^^" if mishka == chris else "Mishka" if mishka > chris else "Chris"


if __name__ == "__main__":

    n = int(raw_input())

    games = list()
    for _ in xrange(0, n):
        games.append(map(int, raw_input().split(" ")))

    print solve(games)
