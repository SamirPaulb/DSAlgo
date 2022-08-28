# https://leetcode.com/problems/median-of-two-sorted-arrays/

# -------------------- Method 1 --------- NOT Optimised O(N) Time----------------
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1); n2 = len(nums2)
        mid = (n1 + n2) // 2  
        i = 0; j = 0
        val, preVal = 0, 0
        
        for k in range(mid+1):
            if i < n1 and j < n2:
                if nums1[i] <= nums2[j]:
                    val = nums1[i]  
                    i += 1
                else:
                    val = nums2[j]
                    j += 1
            elif i < n1:
                val = nums1[i]
                i += 1
            else:
                val = nums2[j]
                j += 1
            
            if k == mid - 1:
                preVal = val
        
        if (n1+n2) % 2 == 0:
            return (val + preVal) / 2
        return float(val)
    
# Timw: O(N)
# Space: O(1)



# -------------------- Method 2 --------- Optimised O(log(N)) Time----------------

# https://www.youtube.com/watch?v=NTop3VTjmxk
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1);   n2 = len(nums2) 
        if n1 > n2: return self.findMedianSortedArrays(nums2, nums1) # WE SHALL DO BINARY SEARCH ON THE SMALLER ARRAY, NUMS1
        
        INT_MIN, INT_MAX = -2**64, 2**64  # SETUP INT_MIN AND INT_MAX FOR EMPTY LEFT / RIGHT PARTITION
        low = 0;   high = n1  # pointers for BINARY SEARCH ON THE SMALLER ARRAY NUMS1
        
        while low <= high:
            
            # GET THE PARITIONS POINTS OF BOTH ARRAYS
            cut1 = (low + high) // 2          # partition of nums1
            cut2 = (n1 + n2 + 1) // 2 - cut1  # partition of nums2
            
            # GET THE 4 BOUNDARY NUMBERS
            left1 = nums1[cut1-1] if cut1 > 0 else INT_MIN   # left1 is the left partition of cut1
            right1 = nums1[cut1] if cut1 < n1 else INT_MAX   # right1 is the right partition of cut1
            
            left2 = nums2[cut2-1] if cut2 > 0 else INT_MIN   # left2 is the left partition of cut2
            right2 = nums2[cut2] if cut2 < n2 else INT_MAX   # right2 is the right partition of cut2
            
            # CORRECT PARTITION FOUND
            if left1 <= right2 and left2 <= right1:  # Got the Answer => Median
                if (n1 + n2) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            
            # MOVE cut1 (mid of binary search) LEFTWARDS
            elif left1 > right2:
                high = cut1 - 1
                
            # MOVE cut1 (mid of binary search) RIGHTWARDS   
            else:
                low = cut1 + 1
        
        return 0.0  # For both empty arrays
    
'''
Time Complexity: O(log(n1))  
Space Complexity: O(1)
'''



'''
Input:
[7,12,14,15]
[1,2,3,4,9,11]

Output:
8.00000
'''
