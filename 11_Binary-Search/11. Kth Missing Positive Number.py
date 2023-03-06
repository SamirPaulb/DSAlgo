# https://leetcode.com/problems/kth-missing-positive-number/
# https://youtu.be/88k8xa-pSrM

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] < mid+1 + k:
                l = mid + 1
            else:
                r = mid - 1
        
        return l + k
    
    
# Time: O(log(n))
# Space: O(1)
