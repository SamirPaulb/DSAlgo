__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/381/A

Solution: This is very similar to the DP card game problem. Since the numbers are distinct, it avoids
the complex case when both the ends are same and the player would pick the side which exposes the
smaller number for next round. That would require a DP solution. But here we can just simulate the
movement with 2 pointers and update the 2 players' points. 
'''


def solve(n, arr):

    is_serajas_turn = True

    s = 0
    e = n - 1
    seraja = 0
    dima = 0

    while s <= e:

        if arr[s] < arr[e]:
            this_round_point = arr[e]
            e -= 1
        else:
            this_round_point = arr[s]
            s += 1

        if is_serajas_turn:
            seraja += this_round_point
        else:
            dima += this_round_point

        is_serajas_turn = not is_serajas_turn

    return str(seraja) + " " + str(dima)


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    print solve(n, arr)
