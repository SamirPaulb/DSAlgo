# Bubble Sort Algorithm

arr = [12,34,56,8,45,8,3,7,23,7,975,345,7,5,43]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


print(arr)

# Time: O(N^2)
# Space: O(1)