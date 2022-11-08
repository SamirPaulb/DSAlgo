__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1374/C

Solution: Keep a running counter for the balancing of brackets in the string. When a ( is observed, increase it
by 1 and when a ) is observed, decrease it by 1. So at any given point if the counter goes negative, we have
unbalanced brackets due to more ). These brackets need to be moved at the end of the string and we can count 
these occurrences for the moves. When this moves counter is updated, reset the balance counter thereby signifying
the move being done. Finally the answer is the value of this move counter. 
'''


def solve(n, brackets):

    balance_counter = 0
    total_moves = 0

    for i in xrange(0, n):

        balance_counter += 1 if brackets[i] == '(' else -1

        if balance_counter < 0:
            total_moves += 1
            balance_counter = 0

    return total_moves


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        brackets = raw_input()
        results.append(solve(n, brackets))

    for result in results:
        print result
