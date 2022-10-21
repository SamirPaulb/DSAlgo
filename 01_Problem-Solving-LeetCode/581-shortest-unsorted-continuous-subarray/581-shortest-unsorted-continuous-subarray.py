class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minL = float("inf")
        maxR = float("-inf")
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                minL = min(minL, nums[i+1])
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                maxR = max(maxR, nums[i])
        
        if minL == float("inf"):  # if minL does not exist then maxR will also not exist. as both minL and maxR checks the same condition
            return 0
        
        left = 0; right = len(nums)-1
        
        for i in range(len(nums)-1):
            if nums[i] > minL:
                left = i
                break
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < maxR:
                right = i
                break
        
        return right - left + 1