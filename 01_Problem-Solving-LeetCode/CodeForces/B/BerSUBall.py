__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/489/B

Solution: Idea is sort the boys and girls skills. Now we keep 2 pointers, one each for boys and girls. If the current
indexed partners' skills are compatible (<=1), then we count them as a pair and advance both pointers. Else we advance
the smaller skilled partner's pointer. This is because since the lists are sorted, the smaller skill will be >= to the
next partner in the other list, hence the only chance is to try another partner. 
'''


def solve(n, boys, m, girls):

    boys.sort()
    girls.sort()

    pairs = 0
    boy_idx = 0
    girl_idx = 0

    while boy_idx < n and girl_idx < m:

        if abs(boys[boy_idx] - girls[girl_idx]) <= 1:
            pairs += 1
            boy_idx += 1
            girl_idx += 1
        elif boys[boy_idx] < girls[girl_idx]:
            boy_idx += 1
        else:
            girl_idx += 1

    return pairs


if __name__ == "__main__":

    n = int(raw_input())
    boys = map(int, raw_input().split(" "))
    m = int(raw_input())
    girls = map(int, raw_input().split(" "))
    print solve(n, boys, m, girls)

