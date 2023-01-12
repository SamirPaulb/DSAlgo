# https://leetcode.com/problems/task-scheduler/
# https://youtu.be/s8p8ukTyA2I

class Solution:
    def leastInterval(self, tasks, n):
        taskCnt = collections.Counter(tasks)
        maxHeap = [-cnt for cnt in taskCnt.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = collections.deque()
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time + n))
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
    
    
# Time: O(len(tasks) * n)
