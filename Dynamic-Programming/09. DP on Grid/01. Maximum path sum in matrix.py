# https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1

# Python 3 program for finding max path in matrix
# To calculate max path in matrix

def findMaxPath(mat):

	for i in range(1, N):

		res = -1
		for j in range(M):

			# When all paths are possible
			if (j > 0 and j < M - 1):
				mat[i][j] += max(mat[i - 1][j],
								max(mat[i - 1][j - 1],
									mat[i - 1][j + 1]))

			# When diagonal right is not possible
			elif (j > 0):
				mat[i][j] += max(mat[i - 1][j],
								mat[i - 1][j - 1])

			# When diagonal left is not possible
			elif (j < M - 1):
				mat[i][j] += max(mat[i - 1][j],
								mat[i - 1][j + 1])

			# Store max path sum
			res = max(mat[i][j], res)
	return res

# Driver program to check findMaxPath
N=4
M=6
mat = ([[ 10, 10, 2, 0, 20, 4 ],
		[ 1, 0, 0, 30, 2, 5 ],
		[ 0, 10, 4, 0, 2, 0 ],
		[ 1, 0, 2, 20, 0, 4 ]])
			
print(findMaxPath(mat))



# Time Complexity: O(N*M)


