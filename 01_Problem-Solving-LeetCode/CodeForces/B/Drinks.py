__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/200/B
Solution: Important is to accept inputs in float. Add all the percentages as fractions to a total. Divide it with
the number of drinks. Also, take care to have 12 places of decimals in the answer. Use format for it.
'''


def solve(drinks,percentages):
    total_percentage = 0
    for percentage in percentages:

        total_percentage += (percentage/100)

    return "{0:.12f}".format((total_percentage/drinks)*100)



if __name__ == "__main__":

    drinks = float(input())
    percentages = map(float,raw_input().split(" "))

    print solve(drinks,percentages)