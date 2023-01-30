# https://leetcode.com/problems/longest-happy-string/

# ---------------------- Method 1 ----------------------
class Solution:
    def longestDiverseString(self, a, b, c):
        arr = [[a, 'a'], [b, 'b'], [c, 'c']]
        res = ""
        while True:
            arr.sort()
            i = 1 if len(res) > 1 and res[-2] == res[-1] == arr[2][1] else 2
            if arr[i][0]:
                res += arr[i][1]
                arr[i][0] -= 1
            else:
                break
        
        return res

# Time: O(n)  # n = a + b + c

# ---------------------- Method 2 ----------------------
class Solution:
    def longestDiverseString(self, a, b, c):
        maxHeap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(maxHeap)
        res = ""
        while True:
            c1, s1 = heapq.heappop(maxHeap)
            c2, s2 = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-2] == res[-1] == s1:
                if c2:
                    res += s2
                    c2 += 1
                else:
                    break
            elif c1:
                res += s1
                c1 += 1
            else:
                break
            heapq.heappush(maxHeap, (c1, s1))
            heapq.heappush(maxHeap, (c2, s2))
        
        return res
    
# Time: O(n)  # n = a + b + c
