class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        down = len(matrix) - 1
        res = []
        
        while left <= right and top <= down:
            for i in range(left, right+1):
                res += [matrix[top][i]]
            top += 1
            
            if top > down: break
            
            for i in range(top, down+1):
                res += [matrix[i][right]]
            right -= 1
            
            if left > right: break
            
            for i in range(right, left-1, -1):
                res += [matrix[down][i]]
            down -= 1
                        
            for i in range(down, top-1, -1):
                res += [matrix[i][left]]
            left += 1
        
        return res