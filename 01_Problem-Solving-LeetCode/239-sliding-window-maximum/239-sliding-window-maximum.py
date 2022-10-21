class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        
        for i in range(len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
                
            if q and i - q[0] >= k:
                q.popleft()
                
            q.append(i)
            
            if i >= k-1: res.append(nums[q[0]])
        
        return res
            
        