class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        l = 0; r = len(nums)
        mid = l + (r - l) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.mergeSortedArrays(left, right)
    
    def mergeSortedArrays(self, a, b):
        if not a or not b: return b or a
        arr = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                arr.append(a[i])
                i += 1
            else:
                arr.append(b[j])
                j += 1
        while i < len(a):
            arr.append(a[i])
            i += 1
        while j < len(b):
            arr.append(b[j])
            j += 1
        return arr