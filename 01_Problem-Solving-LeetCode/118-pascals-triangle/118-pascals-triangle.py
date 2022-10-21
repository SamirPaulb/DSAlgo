class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        
        res = [[1], [1,1]]
        for i in range(3, numRows+1):
            arr = [1]*i
            for j in range(1, i-1):
                arr[j] = res[-1][j-1] + res[-1][j]
            res.append(arr)
        
        return res