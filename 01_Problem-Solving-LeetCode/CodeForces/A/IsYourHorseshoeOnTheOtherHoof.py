__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/228/A

Solution: We want to find the unique colors of the horse shoes present, and that should be subtracted from 4 (for four
legs of the horse). That is number of colors we need to have distinctly colored horse shoes.
'''


def solve(horseShoes):

    uniqueHorseShoes = set()
    uniqueHorseShoes.update(horseShoes)
    return 4 - len(uniqueHorseShoes)


if __name__ == "__main__":

    horseShoes = map(int, raw_input().split(" "))
    print solve(horseShoes)

