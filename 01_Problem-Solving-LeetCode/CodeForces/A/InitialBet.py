__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/478/A

Solution: Since every player is given same amount of coins, the total coins at the end of the game should still be 
divisible by the total number of players. Check and return the result accordingly. Take care of the total coins as 0 case
separately. 
'''

def solve (num):

    n = len(num)
    sum = 0
    for num in nums:
        sum += num

    return -1 if sum == 0 or sum % n != 0 else sum / n



if __name__ == "__main__":

    nums = map(int,raw_input().split(" "))
    print solve(nums)
