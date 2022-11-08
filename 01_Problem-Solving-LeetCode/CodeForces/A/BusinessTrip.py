__author__ = 'deveshbajpai'
'''
Problem Url: http://codeforces.com/problemset/problem/149/A

Algorithm: Sort the list of monthly growth in reverse order. Traverse the list and add monthly growth. In every
iteration track if the count is equal or greater than required growth (k). If so break from the iteration.
While returning the final check, check for it again and return either the count of months or -1 accordingly.
'''


def solve(k, i_list):

    _k = months = 0
    if k == 0:
        return months
    i_list.sort(reverse=True)
    for i in i_list:
        if _k >= k:
            break
        else:
            _k += i
            months += 1

    if _k >= k:
        return months
    else:
        return -1

if __name__ == "__main__":
    k = int(raw_input())
    i_list = map(int,raw_input().split(" "))
    print solve(k,i_list)