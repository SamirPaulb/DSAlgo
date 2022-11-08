__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1339/B

Solution: Sort the array. Keep 2 pointers left and right. Take the pair of elements of these pointed elements
in the result array. Move the left leftwards and right rightwards. This ensures the net distance on the 
number line is smallest, thereby agreeing to the constraint of absolute differences of pair elements.

For odd length arrays, we keep the middle element as the first element in the result array since it cannot
be paired. And then we start from the pointers movement as mentioned above.  
'''


def solve(n, arr):

    arr.sort()

    result = [None] * n

    if n % 2 == 0:
        left = n/2 - 1
        right = n/2
        i = 0
    else:
        left = (n-1)/2 - 1
        right = (n-1)/2 + 1
        result[0] = arr[n/2]
        i = 1

    while left >= 0 and right < n:

        result[i] = arr[left]
        i += 1
        left -= 1

        result[i] = arr[right]
        i += 1
        right += 1

    return " ".join(str(_) for _ in result)


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        results.append(solve(n, arr))

    for result in results:
        print result
