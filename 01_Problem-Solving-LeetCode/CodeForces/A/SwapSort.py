__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/489/A

Solution: Create a sorted copy of the array. Iterate over the array and check if the current indexed element
is same as the one in its sorted version. If not, we need to swap. Hence iterate on the sub-array on the right
of this element to find its swap partner. Find it and swap the given array. Each of these swaps are captured
for the final answer. 
'''


def solve(n, arr):

    sorted_arr = sorted(arr)

    swaps = list()

    for i in xrange(0, n):

        if arr[i] != sorted_arr[i]:

            for j in xrange(i+1, n):

                if arr[j] == sorted_arr[i]:

                    arr[i], arr[j] = arr[j], arr[i]
                    swaps.append([i, j])
                    break

    swaps_count = len(swaps)
    ans = str(swaps_count)
    if swaps_count != 0:
        ans += "\n" + "\n".join(str(swap[0]) + " " + str(swap[1]) for swap in swaps)

    return ans


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    print solve(n, arr)
