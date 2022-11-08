__author__ = 'deveshbajpai'
'''
http://codeforces.com/problemset/problem/136/A

Solution: The idea is to find the value at ith index in the input list (p_arr), shift it from indexed
1 to 0, and use that as index in the result list with value equal to ith index, and shift that from
indexed 0 to 1. 
'''


def solve(n, p_arr):
    result = [0] * n

    for i in xrange(0, n):
        result[p_arr[i]-1] = i+1

    return " ".join(str(elem) for elem in result)


if __name__ == "__main__":

    n = int(raw_input())
    p_arr = map(int, raw_input().split(" "))
    print solve(n, p_arr)
