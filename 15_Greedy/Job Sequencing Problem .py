# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

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
        jobs.sort(key = lambda x:x[2], reverse = True)
        res = count = 0
        booked = set()
        
        for i, d, p in jobs:
            j = d
            while j in booked:
                j -= 1
            if j <= 0: continue
            booked.add(j)
            res += p
            count += 1
        
        return count, res


# Time: O(N log(N)) + O(N * M)    # where N = len(jobs); M = maxDeadline
# Space: O(M)
