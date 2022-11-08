__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/992/A
Solution: Observe closely on few examples. The problem boils down to find the no. of unique elements in the given
array. But the catch is, we don't need to change the already 0 elements. Hence, count the unique elements - 1 (if 
zeroes are present, else 0).
'''

def solve(arr):

    arrSet = set(arr)
    isZeroElemPresent = False

    for a in arrSet:
        if a == 0:
            isZeroElemPresent = True
            break

    return len(arrSet) - (1 if isZeroElemPresent else 0)


if __name__ == "__main__":
    n = int(raw_input())
    arr = map(int,raw_input().split(" "))
    print solve(arr)