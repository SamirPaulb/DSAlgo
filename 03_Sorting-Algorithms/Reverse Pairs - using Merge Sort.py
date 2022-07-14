# https://leetcode.com/problems/reverse-pairs/

class Solution:
    def __init__(self):
        self.count = 0
    
    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        return self.count
    
    def mergeSort(self, nums):
        if len(nums) > 1:
            # calculate mid
            mid = len(nums) // 2
            # divide the input array in to right and left
            left = nums[:mid]
            right = nums[mid:]
            
            self.mergeSort(left)
            self.mergeSort(right)
            
            # the tricky part - updating the count of number of possible pairs
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                self.count += j
            
            # merge two sorted array
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    k += 1
                    i += 1
                else:
                    nums[k] = right[j]
                    k += 1
                    j += 1
            while i < len(left):
                nums[k] = left[i]
                k += 1
                i += 1
            while j < len(right):
                nums[k] = right[j]
                k += 1
                j += 1

# Time: O(n log(n))
# Space: O(n)
