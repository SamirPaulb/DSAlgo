# Theory: https://youtu.be/zPtI8q9gvX8
# Approach: https://youtu.be/LjPx4wQaRIs

''' 
Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60

Input:
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)}
Output:
2 127
'''

class Solution:
    def JobScheduling(self,jobs,n):
        # Sort based on the profit in decending order
        jobs.sort(key = lambda x:x[2])
        
        maxDeadline = 0
        for job in jobs:
            maxDeadline = max(maxDeadline, job[1])
        
        jobDone = [False] * (maxDeadline + 1)
        
        jobsCount = 0
        totalProfit = 0
        for job in jobs:
            for i in range(job[1], 0, -1):
                if jobDone[i] == False:
                    jobsCount += 1
                    totalProfit += job[2]
                    jobDone[i] == True
                    break
        
        return jobsCount, totalProfit

# Time: O(N log(N)) + O(N * M)    # where N = len(jobs); M = maxDeadline
# Space: O(M)