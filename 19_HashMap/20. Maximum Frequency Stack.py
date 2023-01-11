# https://leetcode.com/problems/maximum-frequency-stack/
# https://youtu.be/Z6idIicFDOE

'''
import heapq
class FreqStack:

    def __init__(self):
        self.cnt = collections.Counter()
        self.maxHeap = []
        self.indx = 0

    def push(self, val):
        self.cnt[val] += 1
        self.indx += 1
        heapq.heappush(self.maxHeap, (-self.cnt[val], -self.indx, val))
        
    def pop(self):
        val = self.maxHeap[0][2]
        self.cnt[val] -= 1
        heapq.heappop(self.maxHeap)
        return val
        
# Time: O(log(N))
# Space: O(N)
'''

class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.stacks = {}
        self.maxCnt = 0

    def push(self, val):
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt
        if self.maxCnt < valCnt:
            self.maxCnt = valCnt
            self.stacks[valCnt] = []
        self.stacks[valCnt].append(val)

    def pop(self):
        # print(self.stacks)
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxCnt]: 
            self.maxCnt -= 1
        return res
    
    
# Time: O(1)
# Space: O(N)
