class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            nums[i] = str(nums[i])
        # Bubble Sort
        for k in range(n):
            for i in range(n-1):
                if nums[i] + nums[i+1] < nums[i+1] + nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        
        ans = "".join(nums)
        return ans if int(ans) != 0 else "0"