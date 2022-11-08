__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/959/A

Solution: The standard technique is that based on the number being even or odd, players chose
the entire number and subtract it from itself. This causes the number turn zero thereby causing
the opponent to lose. 
'''


def solve(n):

    return "Mahmoud" if n % 2 == 0 else "Ehab"


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)
