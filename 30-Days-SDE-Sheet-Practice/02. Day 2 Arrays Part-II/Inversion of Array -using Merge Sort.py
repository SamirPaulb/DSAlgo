# https://www.codingninjas.com/codestudio/problems/count-inversions_615
# https://youtu.be/uojx--MK_n0
''' 
Use Merge Sort to reduce the time complexity from O(n^2) to O(n log(n))
In the merge function we check if the left array pointer is greater than right array pointer
then all elements right-side of left array pointer will be greater as both of the arrays are sorted.
'''

from os import *
from sys import *
from collections import *
from math import *

class Solution:
    def __init__(self):
        self.count = 0

    def getInversions(self, arr, n):
        self.count = 0
        self.mergeSort(arr)
        return self.count

    def mergeSort(self, arr):
        if len(arr) > 1:
            #  mid is the point where the array is divided into two subarrays
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]

            # Sort the two halves
            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0

            # Until we reach either end of either left or right, pick larger among
            # elements left and right and place them in the correct position at A[p..r]
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    self.count += mid - i
                    arr[k] = right[j]
                    j += 1
                k += 1

            # When we run out of elements in either left or right,
            # pick up the remaining elements and put in A[p..r]
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1


# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


sol = Solution()
# Main.
arr, n = takeInput()
print(sol.getInversions(arr, n))

# Time: O(n log(n))    # log(n) for deviding into 2 parts and n for linear traversing
# Space: O(n)          # as everytime we are taking new array left and right