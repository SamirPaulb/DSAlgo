# https://youtu.be/nZe7P674xZo

arr = [[ 1, 1, 1, 1, 1 ],
       [ 1, 1, 1, 1, 1 ],
       [ 1, 1, 1, 1, 1 ],
       [ 1, 1, 1, 1, 1 ]]

# Formula: arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]  # as arr[i-1][j-1] got repeated 2 tiems

for i in range(1, len(arr)):
    arr[i][0] += arr[i-1][0]

for j in range(1, len(arr[0])):
    arr[0][j] += arr[0][j-1]

for i in range(1, len(arr)):
    for j in range(1, len(arr[0])):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

    print(arr[i])


# Time: O(N*M)
# Space: O(1)