__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/466/A
Algorithm:
CASE A: res1
Find the total no of tickets that can be brought using group ticket (p)
with rate (b). Add them to result and now check that if its less expensive to buy the remaining tickets using group
ticket or individual ticket. Choose the smaller and add to the result.
CASE B: res2
Just multiply the total quantity with the individual rate
'''
n, m, a, b = map(int,raw_input().split(" "))
res1 = 0
res2 = 0


p = n/m

res1 += p*b
if(n%m!=0):
    if((n-(m*p))*a < b):
        res1 += (n-(m*p))*a
    else:
        res1 += b

res2 = n*a
print min(res1,res2)
