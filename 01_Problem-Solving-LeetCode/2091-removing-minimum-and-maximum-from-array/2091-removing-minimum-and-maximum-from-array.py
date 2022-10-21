class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = max(nums)
        maxInd = nums.index(maxi)
        
        mini = min(nums)
        minInd = nums.index(mini)
        
        both = min(maxInd, minInd) + 1 + n - max(maxInd, minInd)       
        back = n - min(maxInd, minInd)
        front = max(maxInd, minInd) + 1
        
        return min(both, back, front)