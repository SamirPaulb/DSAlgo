# https://leetcode.com/problems/mice-and-cheese/
'''
We want to maximize the total reward by selecting 'k' values from reward1 and everything remaining from reward2. To achieve this, we need to carefully choose values from reward1, as selecting an index in reward1 will make that index unavailable in reward2.

To determine the best selection, we first calculate the differences between the corresponding elements of reward2 and reward1. Then, we identify the 'k' largest positive differences, which indicate the most optimal selections from reward1.

Consider the example with reward1 = [4, 2, 1] and reward2 = [2, 5, 10]. The differences are calculated as follows: 2 - 4 = -2, 5 - 2 = 3, 10 - 1 = 9, resulting in the array [(-2, 0), (3, 1), (9, 2)]. Notice that we keep track of the index by storing tuples (value, index). In this case, if k = 2, we should select the values 4 and 2 from reward1, as they correspond to the largest positive differences. Next, we can take the remaining available value from reward2, which is 10.

By following this approach, we can achieve the maximum total reward, which is the sum of these values: 4 + 2 + 10 = 16.
'''

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        output = 0
        n = len(reward1)
        heap = []
        for i in range(n):
            heap.append((reward2[i] - reward1[i], i))
            
        heapq.heapify(heap)
        visited = set()
        while k:
            k -= 1
            _, idx = heapq.heappop(heap)
            visited.add(idx)
            output += reward1[idx]
            
        # If there is anything left that has not been taken, we take it from reward2.
        for idx, val in enumerate(reward2):
            if idx in visited:
                continue
            output += val
        
        return output
