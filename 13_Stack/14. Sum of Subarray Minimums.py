#https://leetcode.com/problems/sum-of-subarray-minimums/
# https://www.youtube.com/watch?v=Ulb3ixSpE4Y

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
        # Brute Force 
        res = 0
        for i in range(len(arr)):
            min = arr[i]
            for j in range(i, len(arr)):
                if arr[j] < min:
                    min = arr[j]
                res += min
        
        return res
        # Time: O(n^2)
        # Spacee: O(1)
        '''
        # Using the method of Trap Rain Water Problem
        leftMin = []
        lStack = []
        # Filling leftMin => How many left subarray possible left side of curr whose minimum is curr
        for i in range(len(arr)):
            curr = arr[i]
            currCount = 1
            while lStack and lStack[-1][0] > curr:
                peak = lStack.pop()
                currCount += peak[1]
            lStack.append((curr, currCount))
            leftMin.append(currCount)
            
        rightMin = []
        # Filling rightMin => How many right subarray possible right side of curr whose minimum is curr
        rStack = []
        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            currCount = 1
            while rStack and rStack[-1][0] >= curr:
                peak = rStack.pop()
                currCount += peak[1]
            rStack.append((curr, currCount))
            rightMin.append(currCount)
        rightMin = rightMin[::-1]
        
        # Calculating result
        # value = (value of current element) * (number of times curr appears in left subarray) * (number of times curr appears in right subarray)
        # => value = arr[i] * l * r
        res = 0
        for i in range(len(arr)):
            l = leftMin[i]
            r = rightMin[i]
            res += arr[i] * l * r
        
        return res % (10**9 + 7)
        