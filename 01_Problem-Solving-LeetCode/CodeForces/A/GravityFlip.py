__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/405/A

Solution: When the gravity is switched to right-side, we basically align each layer in the box columns in ascending 
order from left to right. Therefore, we need to sort the columns and just return them.

~ Tidbit ~
Python has cool one liners specially when using lambdas. Here we use one that can process elements of an iterable. 
The format is:
operation(variable) for variable in iterable
'''


def solve(columnHeights):

    return " ".join(str(columnHeight) for columnHeight in sorted(columnHeights))


if __name__ == "__main__":

    n = int(raw_input())
    columnHeights = map(int, raw_input().split(" "))
    print solve(columnHeights)
