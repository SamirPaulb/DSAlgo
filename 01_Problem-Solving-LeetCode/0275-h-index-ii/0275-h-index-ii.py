class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0; r = len(citations)-1; n = len(citations)
        while l <= r:
            mid = l + (r - l) // 2
            if citations[mid] == n - mid: return citations[mid]
            elif citations[mid] > n-mid: 
                r = mid - 1
            else:
                l = mid + 1
        
        return n - l