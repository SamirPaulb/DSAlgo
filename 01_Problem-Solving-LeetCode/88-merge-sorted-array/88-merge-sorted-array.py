'''
GAP Algorithm

Approach:
Initially take the gap as ceil() of (m+n)/2
Take as a pointer1 = 0 and pointer2 = gap.
Run a oop from pointer1 &  pointer2 to  m+n and whenever arr[pointer2] < arr[pointer1], swap those.
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
