'''
https://codeforces.com/problemset/problem/1409/B

Solution: The greedy choice to is try to reduce a till x if we have enough rounds to use. Then we use the remaining rounds
to reduce b as much as we can. This gets one set of values of a and b reduced and we can get their product. We do another
round of this calculation where we prefer to reduce b first and then a. The minimum of these two products gives the minimum
possible product.  

''' 


def solve(a, b, x, y, n):

    min1 = calc_min_moves(a, b, x, y, n) # prefer a over b to be reduced first
    min2 = calc_min_moves(b, a, y, x, n) # prefer b over a to be reduced first

    return min(min1, min2)


def calc_min_moves(a, b, x, y, n):

    moves_a = min(n, a - x)
    moves_b = min(n - moves_a, b - y)

    reduced_a = a - moves_a
    reduced_b = b - moves_b

    return reduced_a * reduced_b


if __name__ == "__main__":

    t = int(input())

    results = []
    for _ in range(t):
        a, b, x, y, n = map(int, input().split(" "))
        results.append(solve(a, b, x, y, n))

    for result in results:
        print(result)
