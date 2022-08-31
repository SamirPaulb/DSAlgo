# https://leetcode.com/problems/sort-colors/
# https://youtu.be/oaVa-9wmpns
'''
Dutch National Flag Algorithm:

Use 3 pointers named low, mid, and high to move 0s to the left and 2s to the right and 1s in the middle of the array and hence the array will be sorted. 
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        mid = 0
        right = len(nums) - 1
        
        while mid <= right:
            if nums[mid] == 0:   # need to keep this 0 at low's place
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1

            elif nums[mid] == 2: # need to keep 2 this 2 at high's place
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
                mid -= 1

            mid += 1
        
        return nums

# Time: O(N)  # One Pass Solution
# Space: O(1)

