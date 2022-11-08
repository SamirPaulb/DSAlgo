__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/110/A
Solution: Take number input as String. Build a digit-frequency map of it. Count the frequency
pf 4 and 7. If its either 4 or 7, print YES. Else, print NO.
'''
from collections import Counter

if __name__ == "__main__":

    #take number as string
    num = raw_input()

    digitMap = Counter(num)
    count = digitMap['4']+digitMap['7']
    if(count==4 or count==7):
        print "YES"
    else:
        print "NO"

