__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/791/A

Solution: Nothing fancy. Just run a loop till Limak's weight surpasses that of Bob's. Keep incrementing year in every
iteration. 

'''

def solve(l, b):

    years = 0

    while l <= b:
        l *= 3
        b *= 2
        years += 1

    return years


if __name__ == "__main__":
    l,b = map(int,raw_input().split(" "))
    print solve(l,b)