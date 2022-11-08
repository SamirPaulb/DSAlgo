__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/472/C

Solution: We stick to a greedy strategy of choosing lexicographically smallest handle so that
we are keeping enough lexicographical space for future handles, and enough to be greater than
the previous one. 
Using this, we pick the smaller of first and last name of first name as the handle. Then as
we proceed in the permutation, we choose the current name's handle in the same way. If its
smaller than the previous name's handle, we pick the larger one. If its still smaller than
the previous name's handle, there is no way we can arrange this permutation. Hence we return 
NO. If all the names in the permutation are validated, we return YES. 
'''


def solve(n, names, p):

    first_idx = p[0] - 1 # converting 1-indexing to 0-indexing
    last_handle = min(names[first_idx][0], names[first_idx][1])

    for i in xrange(1, n):

        curr_idx = p[i] - 1 # converting 1-indexing to 0-indexing
        curr_handle = min(names[curr_idx][0], names[curr_idx][1])
        if curr_handle < last_handle:
            curr_handle = max(names[curr_idx][0], names[curr_idx][1])
            if curr_handle < last_handle:
                return "NO"

        last_handle = curr_handle

    return "YES"


if __name__ == "__main__":

    n = int(raw_input())

    names = list()
    for _ in xrange(0, n):
        name = raw_input().split(" ")
        names.append(name)
    p = map(int, raw_input().split(" "))

    print solve(n, names, p)
