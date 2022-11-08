__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/455/A

Solution: We first calculate the frequency map of the array and the maximum element in that.   
freq_map[arr[i]]= frequency of occurrence of arr[i] element

The recurrence can be observed as:
dp[num]= maximum points that can be obtained by considering elements numerically equal to num

To compute that, there can be 2 possibilities:

case 1: num is selected
In this case, we would select all the occurrences of element num in the array to gather that much points. 
Also, the problem would reduce to f(1.... num-2) since all occurrences of num-1 would be deleted as well.

So points scored in this case = num * freq_map[num] + dp[num-2]

case 2: num is not selected
In this case, the strategy would be to move over to the next element to score points which would be num-1.

So points scored in this case = dp[num-1]

So thus we get the recurrence relation is:
 dp[num] = max(dp[num-1] , dp[num-2] + freq_map[num]*num)
 
'''


def solve(n, arr):

    max_elem = 100000 #highest value allowed for an element
    freq_map = [0] * (max_elem + 1)

    for i in xrange(0, n):
        freq_map[arr[i]] += 1

    dp = [0] * (max_elem + 1)
    dp[0] = 0
    dp[1] = freq_map[1]

    for num in xrange(2, max_elem + 1):
        dp[num] = max(dp[num-1], dp[num-2] + num * (freq_map[num]))

    return dp[max_elem]


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    print solve(n, arr)
