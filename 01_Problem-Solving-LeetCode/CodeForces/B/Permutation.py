__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/137/B
Solution: Input the numbers as a integer list.
Now, dump the numbers of list in a set (only if they are less than or equal to n ).
The set preserves only the unique elements. The difference to list size (n) and set size is number of elements
to be changed to be made valid permuation.
'''

if __name__ == "__main__":
    nums = list()
    n = int(raw_input())
    unique_nums = set()
    nums = map(int, raw_input().split(" "))

    for k in nums:
        if(k<=n):
            unique_nums.add(k)

    print n-unique_nums.__len__()