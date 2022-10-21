class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        maxV = arr[0]
        
        for i, ch in enumerate(arr):
            maxV = max(maxV, ch)
            if i == maxV: res += 1
        
        return res if res != 0 else 1