# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        for i in range(2, numRows + 1):
            tmp = [1] * i
            for j in range(1, i-1):
                tmp[j] = arr[-1][j-1] + arr[-1][j]
            arr.append(tmp)
        
        return arr
