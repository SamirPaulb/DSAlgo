__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1333/B

Solution: The first elements of both arrays should be equal since there won't be any element on the left to 
do any operation. We keep 2 flags to denote if we have seen a 1 or -1 so far (left to right). At any point in
the iteration where the corresponding index elements don't match, we want to check if the appropriate left
element is present (via the flags). If not the decision is made that change is not possible. Early exit on 
this decision flag avoids unnecessary iteration of long arrays. 
'''


def solve(n, arr_a, arr_b):

    # no elements on arr_a[0]'s left to do any operation, exit
    if arr_a[0] != arr_b[0]:
        return "NO"

    is_positive_present = True if arr_a[0] == 1 else False
    is_negative_present = True if arr_a[0] == -1 else False
    is_possible = True

    for i in xrange(1, n):

        # update decision
        if arr_a[i] < arr_b[i]:
            if not is_positive_present:
                is_possible = False
        elif arr_a[i] > arr_b[i]:
            if not is_negative_present:
                is_possible = False

        # early exit
        if not is_possible:
            break

        # update flags
        if arr_a[i] == 1:
            is_positive_present = True
        elif arr_a[i] == -1:
            is_negative_present = True

    return "YES" if is_possible else "NO"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        arr_a = map(int, raw_input().split(" "))
        arr_b = map(int, raw_input().split(" "))
        results.append(solve(n, arr_a, arr_b))

    for result in results:
        print result
