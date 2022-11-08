__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1334/B

Solution: The greedy choice made here is iterate over the people with higher amount of money first. This is because
add the people from the lower end would only bring the average down and not help anyone get 'rich'. Hence we sort
the array and iterate from right to left. We keep the running sum and its associated average till we are >= x. As
soon as the constraint is broken, we cannot add any more people to make the group 'rich'. 
'''


def solve(n, x, arr):

    arr.sort()

    curr_sum = total_rich = 0
    for i in xrange(n-1, -1, -1):
        curr_sum += arr[i]
        curr_avg = float(curr_sum)/ float(n - i)

        if curr_avg >= x:
            total_rich += 1
        else:
            break

    return total_rich


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n, x = map(int, raw_input().split(" "))
        arr = map(int, raw_input().split(" "))
        results.append(solve(n, x, arr))

    for result in results:
        print result
