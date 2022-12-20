
'''
https://codeforces.com/problemset/problem/1206/B

Solution: Convert all the positives into 1, negatives as -1 and zeroes as is.
Now we need to check if we have odd number of negatives. If so, we if have some
zeroes, we take one of those and make it -1 so that even number of -1s multiply
to make +1. If not, we make one of the -1s as +1 using 2 moves. No we have -1s
and +1s multiplying to make +1. What's remaining is zeroes if left any. Convert
all of them as +1s for ease using that much of moves. The total of all these moves
is the final answer.
''' 


def solve(n, arr):

    moves = negatives = zeroes = 0
    for i in xrange(0, n):
        if arr[i] > 0:
            # making them 1
            moves += (arr[i] - 1)
        elif arr[i] < 0:
            # making them -1
            moves += (-1 - arr[i])
            negatives += 1
        else:
            zeroes += 1

    # if odd number of negatives are there
    if negatives % 2 == 1:

        # if we can spare a 0, make it -1, which needs 1 moves
        if zeroes > 0:
            moves += 1
            zeroes -= 1
        # if not, make one of the -1 as +1, which needs 2 moves
        else:
            moves += 2
            negatives -= 1

    # make all zeroes as 1s
    if zeroes > 0:
        moves += zeroes

    return moves


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    print solve(n, arr)
