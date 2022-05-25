# https://www.geeksforgeeks.org/check-if-a-word-exists-in-a-grid-or-not/

''' 
Given a 2D grid of characters and a word, the task is to check if that word exists in the grid or not. A word can be matched in 4 directions at any point.
The 4 directions are, Horizontally Left and Right, Vertically Up and Down. 
'''

r = 4
c = 4

# Function to check if a word exists
# in a grid starting from the first
# match in the grid level: index till
# which pattern is matched x, y: current
# position in 2D array
def findmatch(mat, pat, x, y,
			nrow, ncol, level) :

	l = len(pat)

	# Pattern matched
	if (level == l) :
		return True

	# Out of Boundary
	if (x < 0 or y < 0 or
		x >= nrow or y >= ncol) :
		return False

	# If grid matches with a letter
	# while recursion
	if (mat[x][y] == pat[level]) :

		# Marking this cell as visited
		temp = mat[x][y]
		mat[x].replace(mat[x][y], "#")

		# finding subpattern in 4 directions
		res = (findmatch(mat, pat, x - 1, y, nrow, ncol, level + 1) |
			findmatch(mat, pat, x + 1, y, nrow, ncol, level + 1) |
			findmatch(mat, pat, x, y - 1, nrow, ncol, level + 1) |
			findmatch(mat, pat, x, y + 1, nrow, ncol, level + 1))

		# marking this cell as unvisited again
		mat[x].replace(mat[x][y], temp)
		return res
	
	else : # Not matching then false
		return False

# Function to check if the word
# exists in the grid or not
def checkMatch(mat, pat, nrow, ncol) :

	l = len(pat)

	# if total characters in matrix is
	# less then pattern length
	if (l > nrow * ncol) :
		return False

	# Traverse in the grid
	for i in range(nrow) :
		for j in range(ncol) :

			# If first letter matches, then
			# recur and check
			if (mat[i][j] == pat[0]) :
				if (findmatch(mat, pat, i, j,
							nrow, ncol, 0)) :
					return True
	return False

# Driver Code
if __name__ == "__main__" :

	grid = ["axmy", "bgdf",
			"xeet", "raks"]

	# Function to check if word
	# exists or not
	if (checkMatch(grid, "geeks", r, c)) :
		print("Yes")
	else :
		print("No")

# This code is contributed by Ryuga
