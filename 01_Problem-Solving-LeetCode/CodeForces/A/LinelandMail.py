__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/567/A

Solution: Since the points would be ordered, the minimum distance would be with their either the left or right
neighbor. The max would be with the end points. For the first and last element, we won't have both the neighbors
hence they are handled outside the iteration. 
'''


def solve(n, arr):

    result = list()

    # for the first element
    result.append([arr[1] - arr[0], arr[n-1] - arr[0]])

    # for the elements from index 1 to n-2
    for i in xrange(1, n-1):

        min_dist = min(arr[i] - arr[i-1], arr[i+1] - arr[i])
        max_dist = max(arr[i] - arr[0], arr[n-1] - arr[i])

        result.append([min_dist, max_dist])

    # for the last element
    result.append([arr[n-1] - arr[n-2], arr[n-1] - arr[0]])

    return "\n".join(str(re[0]) + " " + str(re[1]) for re in result)


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    print solve(n, arr)
