__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1324/B

Solution: Since we only want to find the presence of 3 or more length palindrome, we basically need
to check at the minimal a sub-sequence which has same numbers on left and right ends, with any number
in the middle. Hence we run a loop over the array for the left end, and run an inner loop for the
right end starting for next to next element of outer loop. A boolean flag helps find the presence
and terminate the loops early.  
'''


def solve(n, arr):

    is_palindrome_subseq_present = False

    i = 0
    while i < n and not is_palindrome_subseq_present:

        j = i + 2

        while j < n and not is_palindrome_subseq_present:

            if arr[i] == arr[j]:
                is_palindrome_subseq_present = True
            j += 1

        i += 1

    return "YES" if is_palindrome_subseq_present else "NO"


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        results.append(solve(n, arr))

    for result in results:
        print result
