'''
https://www.codechef.com/CDW22021/problems/PPPPPPP9

Ameesha owns a magic box of candies. It is magical because at the end of each month, the number of candies in the box doubles. If there were x candies in the box at the start of a month, then the number of candies at the end of the month would become 2x.

However, immediately after doubling the candies, the magic box eats one of the candies (if available) with a probability of 0.5. This incident happens in every month, except the last month of the year.

Ameesha owns x candies right now. Help her find the expected number of candies she will have in one year. You are given that a year lasts for k+1 months. Find and print the answer modulo 109

+ 7.
Input:

The only line of input contains two integers x and k.

    x = initial number of candies in box
    k + 1 = number of months in a year

Output:

Print a single integer, i.e., the expected number of candies Ameesha will own one year later modulo 109

 + 7.
Constraints

    0≤x,k≤101

8

Sample Input:

2 1
Sample Output:

7
EXPLANATION:

    After the first month there will be 50% probability of 3 candies and 50% probability of 4 candies.
    At the end of the year there will be 6 candies with 50% probability and 8 candies with 50% probability. Hence, the answer for this test case will be (6 + 8) / 2 = 7.

Note

    No candies are eaten by box at end of last month of year.



'''






# Solution 1
"""
x,k = input("").split(' ')
x = int(x)
k = int(k)

def sum1(x,k):
    a = x
    i = 0
    for i in range(k+1):
        if i ==k:
            a = 2*a
        else:
            a = 2*a
            a = a-1
    return a

def sum2(x,k):
    b = x
    j = 0
    for j in range(k+1):
        b = b*2
    return b

TotalCandy = (sum1(x,k) + sum2(x,k))/2


print(int(TotalCandy))

"""





# Solution 2
'''

import sys
arr = list(map(int, input().split()))
n=arr[0]
k=arr[1]
if(n==0):
    print(0)
    sys.exit()
r=(10**9)+7
a=pow(2,k,r)
b=(2*n-1)%r
ans=(a*b)%r
if(ans+1==r):
    print(0)
else:
    print(ans+1)

'''








# Best Solution

a,k=map(int, input(). split())
mod=1000000007
print((pow(2,k+1,mod)*a-pow(2,k,mod)+1)%mod if a>0 else 0)
