__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/373/A
Solution: Create a map via Counter of the panel numbers. Make capacity as 2*k.
Run a loop for all digits and see if there is a case where the value of a digit in the
Counter map is more than the capacity. If so, return NO. If every case is fine, return YES.
'''
from collections import Counter

def solve(capacity,mp):
    for i in range(1,10):
        if(mp[str(i)] > capacity):
            return "NO"

    return "YES"



if __name__ == "__main__":
    k = int(raw_input())
    panels = ""
    for i in range(0,4):
        panels += raw_input()

    mp = Counter(panels)
    #k is the capacity with 1 hand, Total capacity is 2*k (both hands)
    print solve(2*k,mp)

