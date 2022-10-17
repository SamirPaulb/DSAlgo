# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # we use maxHeap so that we can pop largest number among k+1 numbers in maxHeap first
        maxHeap = []

        """
        instead of iterating over all the numbers of both array, we can iterate only
        the first 'K' numbers from both array.

        Since they are sorted in ascending order, the pairs with the minimum sum will
        be just the first 'K' numbers from those two arrays.
        """
        for i in range(0, min(k, len(nums1))):
            for j in range(0, min(k, len(nums2))):
                x = nums1[i]
                y = nums2[j]
                
                # sum of two number
                total = x + y
                
                if len(maxHeap) < k:
                    heapq.heappush(maxHeap, [-total, x, y])
                else:
                    # if the sum of x and y is larger than the largest (among the k smallests)
                    # sum, we can 'break' here. Since the arrays are sorted in the ascending order,
                    # we will not be able to find a pair with smaller sum moving forward.
                    if total > -maxHeap[0][0]:
                        break
                    
                    # push new numbers to the heap
                    heapq.heappush(maxHeap, [-total, x, y])

                    # pop the largest number among k+1 numbers in maxHeap, so that only
                    # k smallest numbers are in maxHeap
                    heapq.heappop(maxHeap)

        result = []
        while maxHeap:
            popped = heapq.heappop(maxHeap)
            result.append([popped[1], popped[2]])

        return result

