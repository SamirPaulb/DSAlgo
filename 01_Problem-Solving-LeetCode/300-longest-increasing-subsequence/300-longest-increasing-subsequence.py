class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        
        def findLeftMostGreaterElementIndex(target):
            l = 0; r = len(arr)-1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        for i in range(n):
            if not arr or arr[-1] < nums[i]:
                arr.append(nums[i])
            else:
                j = findLeftMostGreaterElementIndex(nums[i])
                arr[j] = nums[i]
        
        return len(arr)