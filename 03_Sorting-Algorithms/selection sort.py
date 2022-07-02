# Selection Sort Algorithm

arr = [10, 16, 8, 12, 15, 3, 9, 5]

for i in range(len(arr)):
    mi = i   # index of minimum element in arr[i:]
    for j in range(i+1, len(arr)):
        if arr[mi] > arr[j]:
            mi = j
    # Swap the found minimum element with the first element   
    arr[i], arr[mi] = arr[mi], arr[i]

print(arr)

# Time: O(N^2)
# Space: O(1)

