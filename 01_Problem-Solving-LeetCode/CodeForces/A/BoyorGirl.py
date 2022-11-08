__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/236/A
Solution: Make the set of the input string. If its length is even, its a girl. Else boy.
'''
if(len(set(raw_input()))%2==0):
    print "CHAT WITH HER!"
else:
    print "IGNORE HIM!"
