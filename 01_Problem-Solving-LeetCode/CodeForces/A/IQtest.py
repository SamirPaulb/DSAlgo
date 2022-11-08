__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/25/A
Algorithm: Since the numbers are from 1 to n, one possible way can be considering numbers into 2 buckets: odd and even.
Increase the count by 1 each time of the particular bucket found. Since there is only one different element present,
only one of the bucket count will be 1. Just print its index value (since the question requires index of list from 1),
return found_index+1.
'''

def solve(n,nums):

    even_diffElemIndex = 0
    even_elemCount = 0

    odd_diffElemIndex = 0
    odd_elemCount = 0

    for i in range(0,n):

        if(nums[i]%2==0):
            even_diffElemIndex = i
            even_elemCount+=1
        elif(nums[i]%2!=0):
            odd_diffElemIndex = i
            odd_elemCount+=1

    if(even_elemCount==1):
        return even_diffElemIndex+1
    return odd_diffElemIndex+1






if __name__ == "__main__":
    n = int(raw_input())
    nums = map(int,raw_input().split(" "))
    #print nums

    print solve(n,nums)
