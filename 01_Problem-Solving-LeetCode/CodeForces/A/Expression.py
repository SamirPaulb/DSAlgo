__author__ = 'deveshbajpai'
'''
http://codeforces.com/problemset/problem/479/A
Algorithm: If all the numbers are 1, return 3. If a and c are 1, then we add them all.
If now any of a , b or c are 1, then add it with its next number and multiply with the 3rd number.
Take max of a+b and b+c when b==1.
'''

def solve(a,b,c):
    if(a==1 and c==1):
        return 2+b
    elif(a==1):
        return (a+b)*c
    elif(b==1):
        return max((a+b)*c,a*(b+c))
    elif(c==1):
        return a*(b+c)
    else:
        return a*b*c


if __name__ == "__main__":
    a = input()
    b = input()
    c = input()
    print solve(a,b,c)
