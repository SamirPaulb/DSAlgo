from os import *
from sys import *
from collections import *
from math import *

def mergeSort(arr):
    if len(arr) > 1:
        #  mid is the point where the array is divided into two subarrays
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        # Sort the two halves
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        # Until we reach either end of either left or right, pick larger among
        # elements left and right and place them in the correct position at A[p..r]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
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

    return arr

# Taking inpit using fast I/O.
def takeInput() :
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr

# Main.
arr = takeInput()
print(mergeSort(arr))

# Time: O(n log(n))    # log(n) for deviding into 2 parts and n for linear traversing
# Space: O(n)          # as everytime we are taking new array left and right









''' 
# Merge Sort Algorithm

a = [1,4,45,66,8,89,54,0,5,6,75,675,7,56]

def mergesort(a, l, r):   # l = left, r = right,  m = middle element
    if l < r:
        m = (l+r)//2
        mergesort(a, l, m)
        mergesort(a, m+1, r)
        merge(a, l, m, r)
    return a

def merge(a, l, m, r):
    i = l
    j = m+1
    b = []
    while i <= m and j <= r:
        if a[i] <= a[j]:
            b.append(a[i])
            i += 1
        else:
            b.append(a[j])
            j += 1

    while i <= m:
        b.append(a[i])
        i += 1
    
    while j <= r:
        b.append(a[j])
        j += 1

    for k in range(l, r+1):
        a[k] = b[0]
        b.pop(0)

    
mergesort(a, 0, len(a)-1)
print(a)


'''