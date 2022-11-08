__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/271/A
Algorithm: Brute force solution. Keep increasing the year and create a set of its digits.
If all digits are unique, the size of the set will be 4. If such a case if found, return the
current year value.
'''
def solve(year):
    while(True):
        year = str(int(year)+1)
        if(len(set(year))==4):
            return year

if __name__ == "__main__":
    print solve(raw_input())


