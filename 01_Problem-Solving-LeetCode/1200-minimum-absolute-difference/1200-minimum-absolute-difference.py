class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr.sort()
        mini = 2**31

        for i in range(1, len(arr)):
            mini = min(mini, arr[i] - arr[i-1])
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == mini:
                res.append([arr[i-1], arr[i]])
                
        return res