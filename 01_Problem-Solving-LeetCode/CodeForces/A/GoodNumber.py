__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/365/A
Solution: Brute force solution. Run through the list of numbers and check for each num, if the
thre is a digit from 0 to k which is not present in it, set a flag as true. If anywhere this
flag is set, do not increment count and increment otherwise. Return count in the end.
'''
def solve(n,k,a):
    count = 0
    for num in a:
        notCorrect = False
        for i in range(0,k+1):
            if(str(i) not in num):
                notCorrect = True
                break
        if(not notCorrect):
            count += 1

    return count

if __name__ == "__main__":
    n,k = map(int,raw_input().split(" "))
    _n = 0
    a = list()
    while(_n < n):
        a.append(raw_input())
        _n +=1

    print solve(n,k,a)