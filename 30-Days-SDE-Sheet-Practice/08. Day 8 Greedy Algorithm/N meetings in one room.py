# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#
''' 
We can start a new meeting after its previous meeting ends. So I will 
sort the meeting array based on ending time. So that meetings with low ending time comes fist
'''
class Solution:
    #Function to find the maximum number of meetings that can be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meeting = []
        for i in range(len(start)):
            meeting.append([i, start[i], end[i]])
        meeting.sort(key = lambda x:x[2])
        
        maxMeet = [0]
        prevEnd = meeting[0][2]
        for i in range(1, len(meeting)):
            if meeting[i][1] > prevEnd:
                prevEnd = meeting[i][2]
                maxMeet.append(meeting[i][0])
        
        return len(maxMeet)
        


class Solution:
    def maximumMeetings(self,n,start,end):
        # code here
        time = [[start[i], end[i]] for i in range(len(start))]
        time.sort(key = lambda x : x[1])
        res = 1
        r = 1
        l = 0
        while r < len(time):
            if time[r][0] > time[l][1]:
                res += 1
                l = r
            r += 1
        
        return res

# Time Complexity : O(N*LogN)
# Auxilliary Space : O(N)