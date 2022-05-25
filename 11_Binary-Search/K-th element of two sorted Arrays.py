# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
# https://youtu.be/nv7F4PiLUzo

class Solution:
    def kthElement(self,  nums1, nums2, n, m, k):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2: return self.kthElement(nums2, nums1, n, m, k)
        
        low = max(0, k-n1); high = min(k, n1)
        INT_MIN = -2**31; INT_MAX = 2**31
        
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1
            
            left1 = nums1[cut1-1] if cut1 > 0 else INT_MIN
            right1 = nums1[cut1] if cut1 < n1 else INT_MAX
            
            left2 = nums2[cut2-1] if cut2 > 0 else INT_MIN
            right2 = nums2[cut2] if cut2 < n2 else INT_MAX
            
            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)
            
            elif left1 > right2:
                high = cut1 - 1
            else: 
                low = cut1 + 1
        
        return 1
        
        
# Time: O(log(min(n, m)))
# Space: O(1)