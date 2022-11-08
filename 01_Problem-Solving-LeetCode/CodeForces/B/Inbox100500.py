__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/465/B
Algorithm: Consider the string for 3 cases of unread messages. Follow the comments in
the if ladder.
'''
n = int(raw_input())
str = "".join(raw_input().split(" "))

prev = -1
count = 0

for i in range(0,n):
    if(str[i]=='1'):
        #Case 1: Previous element was present at a distance less than or equal to 2
        # and current unread message is not the first unread message
        if(i-prev<=2 and prev!=-1):
            count += i-prev
        #Case 2: First unread message
        elif(prev==-1):
            count += 1
        #Case 3: Previous element was present at a distance more than 2 and current
        # unread message is not the first unread message of the inbox
        # 2 is added because 1 movement is for returning back to list and other to
        # to come back to read mail view.
        else:
            count += 2
        #update previous found unread message index
        prev = i

print count