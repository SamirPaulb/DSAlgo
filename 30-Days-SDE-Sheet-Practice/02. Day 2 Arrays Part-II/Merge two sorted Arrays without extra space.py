# https://leetcode.com/problems/merge-sorted-array/

# --------------------- Method 1 -----------------------------------
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            
        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1
                 
        return nums1

# Time: O(N)
# Space: O(1)



# --------------------- Method 2 -----------------------------------
'''
GAP Algorithm

Approach:
Initially take the gap as ceil() of (m+n)/2
Take as a pointer1 = 0 and pointer2 = gap.
Run a loop from pointer1 &  pointer2 to  m+n and whenever arr[pointer2] < arr[pointer1], swap those.
After completion of the loop reduce the gap as gap = gap // 2.
Repeat the process until gap > 0.
'''
# https://youtu.be/hVl2b3bLzBw
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # replace the 0's of nums1 with elements of nums2
        for i in range(n):
            nums1.pop()
        nums1 += nums2
            
        gap = ceil((m + n) / 2)
        
        gap1count = 0
        
        while gap > 0:
            i = 0
            j = i + gap
            while j < m + n:
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]
                i += 1
                j += 1
            gap = (gap + 1) // 2
            
            if gap == 1:
                gap1count += 1
                if gap1count > 1: break
                
        return nums1
    
# Time: O(N log(N))
# Space: O(1)



# --------------------- Method 3 -----------------------------------
# Using Insertion method
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if len(nums2) == 0: return nums1
        for i in range(len(nums2)):
            nums1.pop()
        i = 0
        while i < len(nums1):
            if len(nums2) > 0 and nums2[0] <= nums1[i]:
                nums1.insert(i, nums2[0])
                nums2.pop(0)
            i += 1
        
        if len(nums2) > 0:
            nums1 += nums2
            
# Time: O(N)
# Space: O(1)
