# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#
# https://youtu.be/II6ziNnub1Q


class Solution:
    #Function to find the maximum number of meetings that can be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meeting = []
        for i in range(len(start)):
            meeting.append([i, start[i], end[i]])
        
        # We can start a new meeting after its previous meeting ends. So I will
        # sort the meeting array based on ending time. So that meetings with low 
        # ending time comes fist
        meeting.sort(key = lambda x:x[2])
        
        maxMeet = [0]
        prevEnd = meeting[0][2]
        for i in range(1, len(meeting)):
            if meeting[i][1] > prevEnd:
                prevEnd = meeting[i][2]
                maxMeet.append(meeting[i][0])
        
        return len(maxMeet)
        
# Time Complexity: O(N log(N))
# Space Complexity: O(N)
