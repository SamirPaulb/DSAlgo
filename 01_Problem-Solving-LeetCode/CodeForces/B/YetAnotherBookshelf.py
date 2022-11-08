__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1433/B

Solution: Idea is to find the empty spaces between the first and last book. Since the empty spaces between
them would define the shifts needed to bring all the books together. To find the first and last book, we
traverse the bookshelf in left to right and right to left directions respectively. Once those indices are
noted, we traverse between them and count the zeroes. That is the final shift value and returned as the result.
'''


def solve(n, bookshelf):

    shifts = 0

    # traverse left to right and find the index of first book
    i = 0
    while i < n and bookshelf[i] == 0:
        i += 1
    first_book = i

    # traverse right to left and find the index of first book (last book wrt. left to right)
    i = n-1
    while i >= 0 and bookshelf[i] == 0:
        i -= 1
    last_book = i

    # find the empty spaces between the first and last book (excluding those border books)
    for i in xrange(first_book+1, last_book):
        if bookshelf[i] == 0:
            shifts += 1

    return shifts


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n = int(raw_input())
        bookshelf = map(int, raw_input().split(" "))
        print solve(n, bookshelf)
