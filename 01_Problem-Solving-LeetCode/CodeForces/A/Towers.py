__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/37/A
Algorithm: Sort the list of towers. Check if current and previous tower is same. If so increment the length of current
max length. If no, re-initialize the values for current running length and increment the count value.
'''

def solve(n,towers):
    towers = sorted(towers)
    count = 1
    maximum = 1
    curr = 1
    for i in range(1,len(towers)):
        if(towers[i]==towers[i-1]):
            curr+=1
            maximum = max(curr,maximum)
        else:
            curr = 1
            count +=1

    print maximum,count




if __name__ == "__main__":
    n = int(raw_input())
    towers = map(int,raw_input().split(" "))
    solve(n,towers)
