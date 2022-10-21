class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr = sorted(citations); n = len(citations)
        l = 0; r = len(arr)-1
        
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] == n-mid: return arr[mid]
            elif arr[mid] > n-mid:
                r = mid - 1
            else:
                l = mid + 1
        
        return n - l