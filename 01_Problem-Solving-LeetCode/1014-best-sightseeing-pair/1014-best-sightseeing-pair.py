class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        arr = [0]*len(values)
        maxi = -2**31
        res = 0
        for i in range(len(values)-1, -1, -1):
            arr[i] = maxi
            res = max(res, values[i] + i + arr[i])
            maxi = max(maxi, values[i] - i)
        

        '''
       res = 0
        for i in range(len(values)-1):
            res = max(res, values[i] + i + arr[i])
            '''
        return res