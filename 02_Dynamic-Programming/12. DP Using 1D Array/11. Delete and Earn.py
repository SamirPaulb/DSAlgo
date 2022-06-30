# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # This question is SAME as House Robber 1
        # just we need to make an array with total sum of that number
        
        # nums = [2,2,3,3,3,4]
        
        arr = [0] * (max(nums)+1)
        for num in nums:
            arr[num] += num
        # arr = [0, 0, 4, 9, 4]
        
        # now apply house robber 1 on this problem
        
        n = len(arr)
        if n < 3: return max(arr)
        
        for i in range(3, n):
            if i - 3 >= 0: arr[i] += max(arr[i-2], arr[i-3])
            else: arr[i] += arr[i-2]
                
        return max(arr[-1], arr[-2])
    
    
# Time: O(max(nums))
# Space: O(max(nums))
