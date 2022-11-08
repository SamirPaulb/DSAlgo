__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1300/A

Solution: Interesting problem with few cases to handle. 
Lets have totalNoOfZeroes capture the total no. of zeroes in the array, sum as sum and ans as total no. of operations
needed

We iterate over the numbers and calculate totalNoOfZeroes and sum.

Now, if the totalNoOfZeroes is 0, it means product would be non-zero. Hence we only need to concern about the sum being
zero. So we check that and if so, we add 1 to the ans since that 1 operation would add one and make the sum non-zero.

If the totalNoOfZeroes is not 0, it means the product is already zero. That means, we will have to do totalNoOfZeroes 
operations to make those zeroes are ones to make the product non-zero. While doing that, we increased the sum by that, 
hence we add totalNoOfZeroes to sum. Now the sum might be zero, if so we need to do one more operation to make it non
zero. Hence we add 1 to the ans. Else we already have the ans correct.

Finally we return the answer. 

Time Complexity: O(n) 
'''


def solve(t, nums):

    totalNoOfZeroes = sum = ans = 0
    ans = 0

    for num in nums:

        sum += num

        if num == 0:
            totalNoOfZeroes += 1

    if totalNoOfZeroes == 0:

        if sum == 0:
            ans = 1

    else:

        ans = totalNoOfZeroes
        sum += totalNoOfZeroes

        if sum == 0:
            ans += 1

    return ans




if __name__ == "__main__":
    n = int(raw_input())

    answers = []
    for i in xrange(0,n):
      t = int(raw_input())

      nums = map(int, raw_input().split(" "))
      answers.append(solve(t, nums))

    for answer in answers:
        print answer