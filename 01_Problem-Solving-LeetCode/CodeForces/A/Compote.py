__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/746/A

Solution: Each compote needs 1 lemon, 2 apples and 4 pears. Hence, we need to capture the number of such compotes we 
can form. For that we get the quotients of them when divided with their ratios and then taking the min of that. This min
ensure the at-least condition. Since we need to calculate total fruits, we multiply that with no. of fruits in one compote.
'''


def solve(lemons, apples, pears):

    oneCompote = 1 + 2 + 4
    l = lemons/1
    a = apples/2
    p = pears/4

    return min(l,a,p) * oneCompote


if __name__ == "__main__":
    lemons = int(raw_input())
    apples = int(raw_input())
    pears = int(raw_input())
    print solve(lemons, apples, pears)