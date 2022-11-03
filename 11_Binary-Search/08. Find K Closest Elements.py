# https://leetcode.com/problems/find-k-closest-elements/


class Solution:
	def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

		# if the length of the array is the same as k, we can
		# just return the array itself
		if len(arr) == k:
			return arr

		# In this example, we are doing a modified binary search, instead of
		# looking for a particular value, we are looking for a range of a window.

		# we cannot do a regular binary search here because the sliding window
		# will out of index when it slides to the last k elements at the end of
		# the array. Thus, right pointer + k <= len(arr), so right = len(arr) - k
		left, right = 0, len(arr) - k

		# When the left and the right pointer at the same position, we've
		# searched through all possible elements in arr
		while left < right:

			# set midpoint, in this case, the midpoint is the starting point of
			# the sliding window
			mid = (left + right) // 2

			# since midpoint is the starting point of the sliding window, thus
			# the end point of the sliding window is m + k, because we are looking
			# for k elements.
			# use x - arr[m] to determine if the number at midpoint is greater
			# than the number at m + k, which is the end point of the window,
			# notice that we assume the midpoint < x here. If x - arr[m] is greater,
			# which means the number on the left side starts from midpoint is further
			# than the endpoint of the window, we may set left = mid + 1 to continue
			# searching from the right side
			if x - arr[mid] > arr[mid + k] - x:
				left = mid + 1

			# Otherwise, when If x - arr[m] is smaller or equal to the endpoint, 
			# of the window, which means the number on the
			# right side starts at the window endpoint is further than the 
			# starting point of the window, we may set right = mid to continue
			# searching to the left side
			else:
				right = mid
		# After searching through all possible elements, return the sliding window
		# itself, we use start point as left to left + k to return k elements only
		return arr[left : left + k]
