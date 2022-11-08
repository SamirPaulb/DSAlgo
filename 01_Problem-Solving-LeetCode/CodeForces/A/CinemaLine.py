__author__ = 'deveshbajpai'

'''
http://codeforces.com/problemset/problem/349/A
If current person has 25 bill, simply increase the available_25 by 1.
If current person has 50 bill and available_25 is more than equal to 1, simply increase the available_50 by 1 and
decrease available_25 by 1
If current person has 100 bill and either 3 25 bills are available or 1 50 and 1 25 bills are available, adjust the
available_25 and available_50 accordingly along-with increasing available_100 by 1.
Else, return NO.
Base case, when everything is fine, returns YES.
'''
def solve(n,bills):
    avlbl_25 = 0
    avlbl_50 = 0
    avlbl_100 = 0

    for i in xrange(0,n):
        if(bills[i]==25):
            avlbl_25+=1
        elif(bills[i]==50 and avlbl_25>=1):
            avlbl_25-=1
            avlbl_50+=1
        elif(bills[i]==100 and avlbl_25>=1 and avlbl_50>=1):
            avlbl_25-=1
            avlbl_50-=1
            avlbl_100+=1
        elif(bills[i]==100 and avlbl_25>=3):
            avlbl_25-=3
            avlbl_100+=1
        else:
            return "NO"


    return "YES"


if __name__ == "__main__":
    n = input()
    bills = map(int,raw_input().split(" "))
    print solve(n,bills)