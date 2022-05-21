# https://www.codingninjas.com/codestudio/problems/aggressive-cows_1082559?leftPanelTab=1
# https://youtu.be/YTTdLgyqOLY?t=2626
'''
Same binary search approach like 'Minimum Page Allocation Problem'. 
In the isValid function we need to check if with the current distance 'mid'
we can place all the cows in the stalls or not. If we can place all the cows then
try to increase the mid(ie. increase the low). If we can not place all cows then
that distsnce(ie. mid) we need to decrease the distance etween cows ie. dicrease the 
mid.
'''
def aggressiveCows(stalls, k):
	def isValid(mid):
		count = 1  # count of cows
		lastPosition = stalls[0]  # position where we recently placed the cow
		for i in range(1, len(stalls)):
			if stalls[i] - lastPosition >= mid: # checking if we can place cow in this i'th position
				count += 1
				if count == k: return True
				lastPosition = stalls[i]
		return False
	
	stalls.sort()  # as in isValid() function we need the distance in increasing order
	ans = 0
	low = 0
	high = max(stalls)
	while low <= high:
		mid = low + (high - low) // 2
		if isValid(mid):  # check if we can increase the distance or not
			ans = max(ans, mid)
			low = mid + 1
		else:
			high = mid - 1
	
	return ans

# Time: n * log(max(stalls))
# Space: O(1)