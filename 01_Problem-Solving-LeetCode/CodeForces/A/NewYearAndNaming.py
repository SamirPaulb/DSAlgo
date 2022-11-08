__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1284/A

Solution: Basically the array of S and T will repeat in every n and m numbers. Hence of an year Y, 
(Y-1)%n and (Y-1)%m will give the appropriate strings from S and T arrays. The -1 is to match with 
the 0 indexed arrays. 
'''


def solve(n, m, arr_s, arr_t, years):

    str_years = list()

    for year in years:
        # year - 1 for 0 indexed arrays
        str_years.append(arr_s[(year -1) % n] + arr_t[(year -1) % m])

    return "\n".join(str_years)


if __name__ == "__main__":

    n, m = map(int, raw_input().split(" "))
    arr_s = raw_input().split(" ")
    arr_t = raw_input().split(" ")
    q = int(raw_input())
    years = list()
    for _ in xrange(0, q):
        year = int(raw_input())
        years.append(year)
    print solve(n, m, arr_s, arr_t, years)
