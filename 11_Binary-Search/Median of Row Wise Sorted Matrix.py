# https://www.interviewbit.com/problems/matrix-median/
# https://youtu.be/ZN1Ra1pG45E
# https://youtu.be/63fPPOdIr2c

''' 
assigning low = min of matrix and high = max of matrix
we run binary search and try to fing if mid is at middle index of n*m//2 or not.
as rows are sorted so we can use binary search to find right most occurance of the mid to 
find the left side elements count.
'''

class Solution:
	def findMedian(self, matrix):

        def countSmallerThanEqualToMid(row, target):  # like last occurrence index of an element in sorted array 
            l = 0; r = len(row)-1
            while l <= r:
                mid = l + (r - l) // 2
                if row[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        low = 2**31; high = -2**31
        for row in matrix:
            low = min(low, row[0])
            high = max(high, row[-1])

        # if we make an sorted array of all elements of matrix then position of median will be middle index of (n*m)//2 
        medianPosition = (len(matrix) * len(matrix[0])) // 2
        
        while low <= high:
            mid = low + (high - low) // 2
            leftCount = 0
            for row in matrix:
                leftCount += countSmallerThanEqualToMid(row, mid)
            if leftCount <= medianPosition:
                low = mid + 1
            else:
                high = mid - 1
        
        return low


# (high can be maximum of 2**32 and inside that binary search we are counting for each row and inside each row we are using binary search again)
# if n = len(matrix) and m = len(matrix[0])

# Time: log(2^32) * n * log(m) = 32 * n * log(m)
# space: O(1)