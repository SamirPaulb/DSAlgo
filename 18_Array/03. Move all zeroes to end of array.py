# https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1/#
# https://www.geeksforgeeks.org/move-zeroes-end-array/

# Move all zeros to the end
A = [5, 6, 0, 4, 6, 0, 9, 0, 8]
n = len(A)
j = 0

for i in range(n):
	if A[i] != 0:
		A[j], A[i] = A[i], A[j] # Partitioning the array
		j += 1
    
print(A) 

