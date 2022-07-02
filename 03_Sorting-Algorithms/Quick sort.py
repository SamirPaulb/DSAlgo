# Quick Sort Algorithm
# Learn theory: https://youtu.be/7h1s2SojIRw

def partition(arr, l, r):
    p = l
    while l <= r:
        while arr[l] <= arr[p] and l < r:
            l += 1
        while arr[r] >= arr[p] and r > l:
            r -= 1
        if l < r: arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    arr[p], arr[r] = arr[r], arr[p]
    return r

def quicksort(arr, l, r):
    if l >= r: return arr
    j = partition(arr, l, r)
    quicksort(arr, l, j)
    quicksort(arr, j+1, r)

arr = [10, 16, 8, 12, 15, 3, 9, 5]
quicksort(arr, 0, len(arr)-1)
print(arr)


# Average Time: O(N log(N))
# WORST Case TIME Complexity: O(N^2)   

# when the array is already sorted we need to sort it again.
# when the array is already sorted we need to assign pivot to every element and check 
# the whole array so Worst case time is O(N^2)
