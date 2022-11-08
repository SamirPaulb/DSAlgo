__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/214/A
Algorithm: Iterate over the values of a. Check the bounds for both equations with the running value of a.
For the current value of a, calculate the value of b from first equation. Check if these values of a and b satisfy the
second equation; increment the answer count by 1 if so.
'''
def solve(n,m):

    a = 0
    b = 0
    answer = 0
    while(True):
        if(a*a > n or a > m):
            break
        b = a * a - n
        if(b*b + a == m):
            answer+=1
        a+=1
    return answer

if __name__ == "__main__":
    n,m = map(int,raw_input().split(" "))
    print solve(n,m)
